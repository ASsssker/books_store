from django.db import models
from decimal import Decimal
from books.models import Book

# Create your models here.


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=50)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=('-created', ))
        ]
    
    def __str__(self) -> str:
        return f'Order: {self.id}'
    
    def get_total_cost(self) -> Decimal:
        return sum(item.get_cost() for item in self.items.all())
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='orders')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self) -> str:
        return f'{self.id}'
    
    def get_cost(self) -> Decimal:
        return self.price * self.quantity
        
    

