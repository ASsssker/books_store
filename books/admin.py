from django.contrib import admin
from .models import Author, Genre, Book, Commentary

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image', 'book_pdf', 'number_of_pages',
                    'price', 'price', 'release_date']
    list_filter = ['price']
    filter_horizonta = ['author', 'genre']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre_name', 'slug']
    prepopulated_fields = {'slug': ('genre_name',)}


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'status', 'book']