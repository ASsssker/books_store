from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50)
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=('name',))
        ]
    
    def __str__(self) -> str:
        return f'Автор: {self.name}'


class Genre(models.Model):
    genre_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50)
    
    class Meta:
        ordering = ['genre_name']
        indexes = [
            models.Index(fields=('genre_name',))
        ]
    
    def __str__(self) -> str:
        return f'Жанр: {self.genre_name}'
    
    
class Book(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50)
    image = models.ImageField(upload_to='image/books/%Y/%m/%d')
    book_pdf = models.FileField(upload_to='files/books/%Y/%m/%d', blank=True, null=True)
    description = models.TextField()
    number_of_pages = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    auhtor = models.ManyToManyField(Author, related_name='books')
    genre = models.ManyToManyField(Genre, related_name='books')
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=('id', 'slug')),
            models.Index(fields=('name',)),
            models.Index(fields=('-created',))
        ]
        
    def get_absolute_url(self):
        return reverse('books:books_detail', args=[self.id])
    
    def __str__(self) -> str:
        return f'Книга: {self.name}'
    

class Commentary(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    status = models.BinaryField(default=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    
    
    