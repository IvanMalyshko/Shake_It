from django.shortcuts import render, get_object_or_404, redirect
from .models import Cocktail, Ingredient
from cart.forms import CartAddIngredientForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


# SHOP
def home(request):  # все коктели
    cocktail = Cocktail.objects.all()
    return render(request, 'shop/home.html', {'cocktail': cocktail})


def all_ingredients(request):  # все ингы
    ingredient = Ingredient.objects.all()
    return render(request, 'shop/shop.html', {'ingredient': ingredient})


def cocktail_detail(request, cocktail_id):  # коктель детали
    cocktail = get_object_or_404(Cocktail, pk=cocktail_id)
    return render(request, 'cocktail_base/cocktail_detail.html', {'cocktail': cocktail})


def ingredient_detail(request, ingredient_id):  # ингра детали
    ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
    cart_ingredient_form = CartAddIngredientForm()
    return render(request, 'shop/ingredient_detail.html', {'ingredient': ingredient,
                                                           'cart_ingredient_form': cart_ingredient_form})


# AUTH

def singupuser(request):
    if request.method == 'GET':
        return render(request, 'auth/singupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'auth/singupuser.html',
                              {'form': UserCreationForm(),
                               'error': 'That username has already been taken. Please choose new username'})
        else:
            return render(request, 'auth/singupuser.html', {'form': UserCreationForm(),
                                                            'error': 'Password did not match'})
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'auth/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'auth/loginuser.html', {'form': AuthenticationForm(),
                                                           'error':'User name and password did not match'})
        else:
            login(request, user)
            return redirect('home')
