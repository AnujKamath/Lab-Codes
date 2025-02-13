from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # '' corresponds to the root URL
    path('employee-details/', views.employee_details, name='employee_details'),
]
