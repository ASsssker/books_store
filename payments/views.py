
import json
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from orders.models import Order
from .service import create_payment, check_payment_status

# Create your views here.


@require_GET
def payment_process(request):
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id)
    redirect_url = create_payment(request, order)
    return redirect(redirect_url)


@csrf_exempt
@require_POST
def listen_status(request):
    if request.method == 'POST':
        response = json.loads(request.body)
        if check_payment_status(response):
            return HttpResponse(200)
        return HttpResponse(404)