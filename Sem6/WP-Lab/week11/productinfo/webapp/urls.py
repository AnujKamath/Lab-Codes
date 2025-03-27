# webapp/urls.py
from django.urls import path
from .views import create_product, product_list

urlpatterns = [
    path('', product_list, name='product_list'),
    path('create/', create_product, name='create_product'),
]
