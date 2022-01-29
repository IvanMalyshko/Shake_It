from django.shortcuts import render
from django.db.models import Q

from shop.models import Cocktail




def search(request):
    cocktail = Cocktail.objects.filter(Q(title__icontains=request.GET.get('query')) | Q(ingredients__title__icontains=request.GET.get('query')))
    return render(request, 'search/search.html', {'cocktail': cocktail})
