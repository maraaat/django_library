from django.http import HttpRequest
from django.shortcuts import render
from . import models

def show_books(request):
    books = models.Library.objects.all()
    all_books = {
        'books': books
    }
    return render(request, "main/books_show.html", all_books)


def show_one(request, book_id):
    book = models.Library.objects.get(id=book_id)
    temp_book = {
        'book': book
    }
    return render(request,"main/book_show.html", temp_book)