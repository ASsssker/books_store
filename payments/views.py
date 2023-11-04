
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order, OrderItem
from cart.cart import Cart
from .service import create_payment, payment_succesed

# Create your views here.


def payment_process(request):
    order_id = request.session.get('order_id', None)
    order = Order.objects.get(id=order_id)
    redirect_url = create_payment(request, order)
    return redirect(redirect_url)

@csrf_exempt
def listen_status(request):
    if request.method == 'POST':
        response = json.loads(request.body)
        with open('data.json', 'w') as f:
            json.dump(response, f)
        if payment_succesed(response):
            return HttpResponse(200)
        return HttpResponse(404)