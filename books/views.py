from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book

# Create your views here.


class BooksListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/books_list.html'
    
    
class BooksDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/books_detail.html'