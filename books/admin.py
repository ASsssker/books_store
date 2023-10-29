from django.contrib import admin
from .models import Author, Genre, Book, Commentary

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'numver_of_pages', 'price']