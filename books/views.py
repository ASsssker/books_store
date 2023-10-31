from django.shortcuts import render
from django.views.generic.detail import DetailView
from cart.forms import AddBookForm
from .models import Book

# Create your views here.


def books_list(request, author=None, genre=None):
    books = Book.objects.all()
    if author:
        books = books.filter(auhtor__slug=author)
    if genre:
        books = books.filter(genre__slug=genre)
    context = {'books': books}
    return render(request, 'books/books_list.html', context)
    

    
class BooksDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/books_detail.html'
    
    def get_queryset(self):
        return super().get_queryset().prefetch_related('auhtor', 'genre')
    
    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['form'] = AddBookForm() 
        return context
    
    