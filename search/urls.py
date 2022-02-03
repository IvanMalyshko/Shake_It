from django.urls import path

from . import views

app_name='search'

urlpatterns = [
    path('', views.search_cocktail, name='search_cocktail'),
    path('ingredient/', views.search_ingredient, name='search_ingredient'),
]