import uuid
from yookassa import Configuration, Payment
from django.shortcuts import reverse
from django.conf import settings
from orders.models import Order


Configuration.account_id = settings.YOOKASA_SHOP_ID
Configuration.secret_key = settings.YOOKASA_SECRET_KEY


def create_payment(request, order):
    value = str(order.get_total_cost())
    # success_url = request.build_absolute_uri(reverse('payment:completed'))
    # cancel_url = request.build_absolute_uri(reverse('payment:canceled'))
    success_url = reverse('books:books_list')
    
    items = []
    for item in order.items.all():
        temp = {}
        temp['description'] = item.product.name
        temp['quantity'] = item.quantity
        temp['amount'] = {'valye': item.price, 'currency': 'RUB'}
        items.append(temp)
    
    payment = Payment.create({
        'amount':{
            'value': value,
            'currency': 'RUB'
        },
        'confirmation': {
            'type': 'redirect',
            'return_url': success_url
        },
        'payment_method_data': {
            'type': 'bank_card'
        },
        'capture': True,
        'description': f'Заказ №{order.id}',
        'metadata': {
            'order_id': f'{order.id}'
        },
        'receipt': {
            'full_name': f'{order.last_name} {order.first_name}',
            'email': order.email,
        },
        'items':items
    }, uuid.uuid4())
    
    return payment.confirmation.confirmation_url


def payment_succesed(response):
    order_id = response['object']['metadata']['order_id']
    order = Order.objects.get(id=order_id)
    
    if response['event'] == 'payment.succeeded':
        order.paid = True
        order.save()
        
    elif response['event'] == 'payment.canceled':
        order.delete()
    
    return True
