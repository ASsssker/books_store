from decimal import Decimal
from django.conf import settings
from books.models import Book


class Cart:
    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get(settings.CART_ID)
        if not cart:
            cart = self.session[settings.CART_ID] = {}
        self.cart = cart
        
    def add(self, product:Book, quantity: int, ovveride_quantity: bool=False) -> None:
        """Добавить товар в корзину.

        Args:
            product (Book): Товар.
            quantity (int): Добавляемое количество.
            ovveride_quantity (bool, optional): При значении True перезаписывает имеющееся количество на переданное (default False).
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if ovveride_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()
        
    def save(self) -> None:
        """Применить изменения в корзине.
        """
        self.session.modified = True
        
        
    def remove(self, product:Book) -> None:
        """Удалить товар из корзины.

        Args:
            product (Book): Товар.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            
    def clear(self) -> None:
        """Очистить корзину.
        """
        del self.session[settings.CART_ID]
        self.save()
        
    def total_price(self) -> Decimal:
        """Получить суммарную стоимость товаров из корзины.

        Returns:
            Decimal: Суммарня стоимость товаров из корзины.
        """
        return sum(Decimal(item['price']) * item['quantity']
                   for item in self.cart.values())
        
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Book.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
            
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())