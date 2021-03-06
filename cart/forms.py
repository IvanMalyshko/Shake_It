from django import forms

INGREDIENT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddIngredientForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=INGREDIENT_QUANTITY_CHOICES, coerce=int, widget=forms.Select(attrs = {'class':"form-select"}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)