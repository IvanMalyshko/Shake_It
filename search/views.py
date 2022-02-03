from django.shortcuts import render
from django.db.models import Q

from shop.models import Cocktail, Ingredient


def search_cocktail(request):
    query = request.GET.get('query')
    cocktail = Cocktail.objects.filter(Q(title__icontains=query) | Q(ingredients__title__icontains=query))
    number_of_results = len(cocktail)
    return render(request, 'search/search.html', {'cocktail': cocktail, 'number_of_results': number_of_results})

def search_ingredient(request):
    query = request.GET.get('query')
    ingredient = Ingredient.objects.filter(Q(title__icontains=query))
    number_of_results = len(ingredient)
    return render(request, 'search/search_ingredient.html', {'ingredient': ingredient, 'number_of_results': number_of_results})
