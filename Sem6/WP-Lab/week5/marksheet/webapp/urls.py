from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # '' corresponds to the root URL
    path('student-details/', views.student_details, name='student_details'),
]
