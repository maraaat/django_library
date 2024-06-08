from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "main"

urlpatterns = [
    path('books/', views.show_books),
    path('books/<int:book_id>', views.show_one, name="temp_book"),
]
