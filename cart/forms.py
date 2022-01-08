from django import forms

INGREDIENT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)] # определяет выбор тавара для добавления в корзину от 1 до 20


class CartAddIngredientForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=INGREDIENT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)