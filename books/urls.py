from django.urls import path
from .views import BooksListView, BooksDetailView


app_name = 'books'


urlpatterns = [
    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/<int:pk>/', BooksDetailView.as_view(), name='books_detail'),
]
