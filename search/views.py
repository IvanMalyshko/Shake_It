from django.shortcuts import render
from django.db.models import Q

from shop.models import Cocktail


def search(request):
    query = request.GET.get('query')
    cocktail = Cocktail.objects.filter(Q(title__icontains=query) | Q(ingredients__title__icontains=query))
    number_of_results = len(cocktail)
    return render(request, 'search/search.html', {'cocktail': cocktail, 'number_of_results': number_of_results})
