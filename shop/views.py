from django.shortcuts import render, get_object_or_404
from .models import Cocktail, Ingredient, Category
from cart.forms import CartAddIngredientForm


def home(request): # все коктели
    cocktail = Cocktail.objects.all()
    return render(request, 'shop/home.html', {'cocktail': cocktail})


def all_ingredients(request): # все ингы
    ingredient = Ingredient.objects.all()
    return render(request, 'shop/shop.html', {'ingredient': ingredient})


def cocktail_detail(request, cocktail_id): # коктель детали
    cocktail = get_object_or_404(Cocktail, pk=cocktail_id)
    return render(request, 'cocktail_base/cocktail_detail.html', {'cocktail': cocktail})


def ingredient_detail(request, ingredient_id): # ингра детали
    ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
    cart_ingredient_form = CartAddIngredientForm()
    return render(request, 'shop/ingredient_detail.html', {'ingredient': ingredient,
                                                           'cart_ingredient_form': cart_ingredient_form})
