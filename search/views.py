from django.shortcuts import render
from django.db.models import Q
from cart.forms import CartAddIngredientForm
from shop.models import Cocktail, Ingredient


def search_cocktail(request):
    query = request.GET.get('query')
    cocktail = Cocktail.objects.filter(Q(title__icontains=query) | Q(ingredients__title__icontains=query)).distinct()
    number_of_results = str(len(cocktail)) + ' cocktails match your choice'
    return render(request, 'shop/home.html', {'cocktail': cocktail, 'number_of_results': number_of_results})


def search_ingredient(request):
    query = request.GET.get('query')
    ingredient = Ingredient.objects.filter(Q(title__icontains=query)).distinct()
    number_of_results = str(len(ingredient)) + ' ingredients match your choice'
    cart_ingredient_form = CartAddIngredientForm()
    return render(request, 'shop/shop.html',
                  {'ingredient': ingredient, 'number_of_results': number_of_results,
                   'cart_ingredient_form': cart_ingredient_form})
