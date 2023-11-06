from django.urls import path
from .views import BooksListView, BooksDetailView


app_name = 'api'


urlpatterns = [
    path('books/', BooksListView.as_view()),
    path('books/<int:pk>/', BooksDetailView.as_view()),
]
