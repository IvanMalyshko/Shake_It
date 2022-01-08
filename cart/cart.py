from decimal import Decimal
from django.conf import settings
from shop.models import Ingredient


class Cart(object):
    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        ingredient_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        ingredients = Ingredient.objects.filter(id__in=ingredient_ids)
        for ingredient in ingredients:
            self.cart[str(ingredient.id)]['ingredient'] = ingredient

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def add(self, ingredient, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        ingredient_id = str(ingredient.id)
        if ingredient_id not in self.cart:
            self.cart[ingredient_id] = {'quantity': 0, 'price': str(ingredient.price)}
        if update_quantity:
            self.cart[ingredient_id]['quantity'] = quantity
        else:
            self.cart[ingredient_id]['quantity'] += quantity
        self.save()  # сохранение корзины в сесии

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, ingredient):
        """
        Удаление товара из корзины.
        """
        ingredient_id = str(ingredient.id)
        if ingredient_id in self.cart:
            del self.cart[ingredient_id]
            self.save()

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session  # хранение текущей сесии
        cart = self.session.get(settings.CART_SESSION_ID)  # получение корзины с текущей сесии
        if not cart:
            # сохранение пустой корзины в сесии
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True