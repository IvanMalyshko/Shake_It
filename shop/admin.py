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

admin.site.register(Cocktail)
