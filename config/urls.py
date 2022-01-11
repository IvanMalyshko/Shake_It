"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from shop import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    # shop and cocktail_base
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('all_ingredients/', views.all_ingredients, name='all_ingredients'),
    path('cocktail/<int:cocktail_id>/', views.cocktail_detail, name='cocktail_detail'),
    path('ingredient/<int:ingredient_id>/', views.ingredient_detail, name='ingredient_detail'),

    # cart
    path('cart/', include('cart.urls', namespace='cart')),

    # authorization
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
