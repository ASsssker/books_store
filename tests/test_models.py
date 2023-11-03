from django.test import TestCase
from django.utils import timezone
from books.models import Book

DATE_TIME = timezone.now()

class BookModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(name='Test_book', description='Test_description', number_of_pages=1,
                            price=100, release_date=DATE_TIME)
        
    def test_is_object_name(self):
        book =  Book.objects.get(id=1)
        expected_object_name = f'Книга: {book.name}'
        self.assertEqual(expected_object_name, str(book))
        
    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        expected_url = '/books/1/'
        self.assertEqual(expected_url, book.get_absolute_url())