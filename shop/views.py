from django.shortcuts import render, get_object_or_404
from .models import Cocktail, Ingredient, Category


def home(request): # все коктели
    cocktail = Cocktail.objects.all()
    return render(request, 'shop/home.html', {'cocktail': cocktail})


def all_ingredients(request): # все ингы
    ingredient = Ingredient.objects.all()
    return render(request, 'shop/shop.html', {'ingredient': ingredient})


def cocktail_detail(request, cocktail_id): # коктель детали
    cocktail_detail = get_object_or_404(Cocktail, pk=cocktail_id)
    return render(request, '/cocktail_detail.html', {'cocktail_detail': cocktail_detail})


def ingredient_detail(request, ingredient_id): # ингра детали
    ingredient_detail = get_object_or_404(Cocktail, pk=ingredient_id)
    return render(request, 'shop/ingredient_detail.html', {'ingredient_detail': ingredient_detail})
