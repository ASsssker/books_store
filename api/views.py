from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import BookSerializer
from books.models import Book


# Create your views here.
class BooksListView(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    
class BooksDetailView(APIView):
    def get(self, request, pk, format=None):
        book = get_object_or_404(Book, id=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
        
    def put(self, request, pk, format=None):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.update(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'Error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.update()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'Error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)