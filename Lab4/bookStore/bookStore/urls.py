from django.urls import path
from .views import index, bookstore_list, book_add, book_details, book_update, book_delete

urlpatterns = [
    path('', bookstore_list, name="books-list"),
    path('book_add/', book_add, name="book-add"),
    path('book_details/<slug:slug>/', book_details, name="book-details"),
    path('book_update/<slug:slug>/', book_update, name="book-update"),
    path('book_delete/<slug:slug>/', book_delete, name="book-delete"),
]
