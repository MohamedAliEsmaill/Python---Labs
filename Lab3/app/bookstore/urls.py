from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/<int:id>/', views.show, name='show'),
    path('books/create/', views.create, name='create'),
    path('books/edit/<int:id>/', views.edit, name='edit'),
    path('books/delete/<int:id>/', views.delete, name='delete'),
    path('books/store/', views.store, name='store'),
    path('books/update/<int:id>/', views.update, name='update'),
]
