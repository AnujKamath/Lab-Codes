from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_form, name='car_form'),
    path('result/', views.result, name='result'),
]
