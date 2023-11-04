from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_GET
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from cart.forms import AddBookForm
from .models import Book, Commentary
from .forms import AddCommentForm

# Create your views here.


@require_GET
def books_detail(request, pk):
    try:
        book = Book.objects.filter(id=pk).prefetch_related ('auhtor', 'genre').first()
    except ObjectDoesNotExist:
        return Http404()
    comments_q = Commentary.objects.filter(book=book)
    context = {'book': book, 'comments': comments_q, 'book_form': AddBookForm(), 'comment_form': AddCommentForm()}
    return render(request, 'books/books_detail.html', context)


@require_GET
def books_list(request, author=None, genre=None):
    books = Book.objects.all()
    
    if author:
        books = books.filter(auhtor__slug=author)
    if genre:
        books = books.filter(genre__slug=genre)
    
    context = {'books': books}
    return render(request, 'books/books_list.html', context)


@require_POST
def add_comment(request, pk):
    form = AddCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        book = get_object_or_404(Book, id=pk)
        comment.book = book
        comment.save()

    return redirect('books:books_detail', pk)


@require_GET
def search_books(request):
    query = request.GET.get('search')
    search_res = Book.objects.filter(name__icontains=query)
    context = {'books': search_res}
    return render(request, 'books/books_list.html', context)
        