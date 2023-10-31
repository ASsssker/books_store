from django.urls import path
from .views import books_list, BooksDetailView


app_name = 'books'


urlpatterns = [
    path('books/', books_list, name='books_list'),
    path('author/<slug:author>/', books_list, name='author_books'),
    path('genre/<slug:genre>/', books_list, name='genre_books'),
    path('books/<int:pk>/', BooksDetailView.as_view(), name='books_detail'),
]
