from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='media/ingredient/', blank=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Ингредиенты'
        verbose_name_plural = 'Ингредиенты'

    def get_absolute_url(self):
        return reverse('ingredient_detail',
                       args=[self.id])

    def __str__(self):
        return self.title


class Cocktail(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='media/cocktail/', blank=False)
    recipe = models.TextField(blank=True)
    ingredients = models.ManyToManyField(Ingredient)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Коктели'
        verbose_name_plural = 'Коктели'

    def __str__(self):
        return self.title
