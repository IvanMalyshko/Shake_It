from django.urls import path
from . import views

app_name='orders'

urlpatterns = [
    path('orders/create', views.order_create, name='order_create'),
    path('all_orders/', views.all_orders, name='all_orders'),
    path('order_detail/<int:order_id>', views.order_detail, name='order_detail'),
]
