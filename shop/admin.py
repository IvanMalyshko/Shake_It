from django.contrib import admin
from .models import Category, Ingredient, Cocktail


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Category, CategoryAdmin)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']


admin.site.register(Ingredient, IngredientAdmin)


class CocktailAdmin(admin.ModelAdmin):
    list_display = ['title', 'recipe']
    list_display_links = None
    list_editable = ['title', 'recipe']



admin.site.register(Cocktail, CocktailAdmin)
