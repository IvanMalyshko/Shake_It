from django.shortcuts import render, get_object_or_404
from cart.cart import Cart
from orders.forms import OrderCreateForm
from orders.models import Order, OrderItem

# создание заказа из корзины, очистка корзины и редирект
def order_create(request):
    cart = Cart(request) # получение корзины из сессии
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         ingredient=item['ingredient'],
                                         price=item['price'],
                                         quantity=item['quantity'],
                                         )
            # очистка корзины
            cart.clear()
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})


def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_item = get_object_or_404(OrderItem, pk=order_id)
    return render(request, 'orders/order_detail.html', {'order': order, 'order_item': order_item})


def all_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/test_page.html', {'orders': orders})
