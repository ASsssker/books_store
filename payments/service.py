import uuid
from yookassa import Configuration, Payment
from django.shortcuts import reverse, get_object_or_404
from BookStore.settings import YOOKASA_SHOP_ID, YOOKASA_SECRET_KEY, EMAIL_HOST_USER
from orders.models import Order
from .tasks import payment_succeeded


Configuration.account_id = YOOKASA_SHOP_ID
Configuration.secret_key = YOOKASA_SECRET_KEY


def create_payment(request, order):
    value = str(order.get_total_cost())
    success_url = request.build_absolute_uri(reverse('books:books_list'))
    
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


def check_payment_status(response):
    order_id = response['object']['metadata']['order_id']
    order = get_object_or_404(Order, id=order_id)
    
    if response['event'] == 'payment.succeeded':
        order.paid = True
        order.save()
        payment_succeeded.delay(EMAIL_HOST_USER, order.email)
        
    else:
        email = order.email
        order.delete()
        payment_canceled.delay(EMAIL_HOST_USER, email)
    
    # if .....:
        # return False
        
    
    return True
