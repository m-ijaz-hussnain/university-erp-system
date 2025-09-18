from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.manage_books, name='manage_books'),
    path('borrowing/', views.manage_borrowing, name='manage_borrowing'),
]