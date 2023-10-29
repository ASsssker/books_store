from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Genre(models.Model):
    genre_name = models.CharField(max_length=50, unique=True)
    
    
class Book(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50)
    book_pdf = models.FileField(upload_to='books/%Y/%m/%d', blank=True, null=True)
    description = models.TextField()
    number_of_pages = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    auhtor = models.ManyToManyField(Author, related_name='books')
    genre = models.ManyToManyField(Genre, related_name='books')
    

class Commentary(models.Model):
    emil = models.EmailField()
    name = models.CharField(max_length=50)
    status = models.BinaryField(default=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    
    
    