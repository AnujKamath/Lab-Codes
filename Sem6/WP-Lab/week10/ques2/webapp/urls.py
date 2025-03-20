from django.urls import path
from . import views

urlpatterns = [
    path('', views.insert_data, name='insert_data'),
    path('company_query/', views.company_query, name='company_query'),
]
