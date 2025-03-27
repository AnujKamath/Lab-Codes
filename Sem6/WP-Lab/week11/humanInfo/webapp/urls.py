from django.urls import path
from .views import human_list, get_human_details, update_human, delete_human

urlpatterns = [
    path('', human_list, name='human_list'),
    path('get_details/<str:first_name>/', get_human_details, name='get_human_details'),
    path('update/<str:first_name>/', update_human, name='update_human'),
    path('delete/<str:first_name>/', delete_human, name='delete_human'),
]
