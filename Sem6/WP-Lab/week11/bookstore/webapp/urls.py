from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.manage_books, name='manage_books'),  # Main management page for searching books
    path('add-book/', views.add_book, name='add_book'),       # URL to add a new book
    path('add-author/', views.add_author, name='add_author'), # URL to add a new author
    path('add-publisher/', views.add_publisher, name='add_publisher'), # URL to add a new publisher
]
