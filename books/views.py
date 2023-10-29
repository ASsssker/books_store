from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Book

# Create your views here.


class BooksView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/books_list.html'
    