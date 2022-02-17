from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Ingredient, Cocktail
from .cart import Cart
from .forms import CartAddIngredientForm

@login_required(login_url='/login/')
@require_POST
def cart_add(request, ingredient_id):
    cart = Cart(request)
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    form = CartAddIngredientForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(ingredient=ingredient,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cocktail_all_ingredients_add(request, cocktail_id):
    cart = Cart(request)
    cocktail = get_object_or_404(Cocktail, id=cocktail_id)
    for ingredient in cocktail:
        cart.add(ingredient)
    return redirect('cart:cart_detail')


def cart_remove(request, ingredient_id):
    cart = Cart(request)
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    cart.remove(ingredient)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})