from django.shortcuts import render, redirect, reverse
from cart.cart import Cart
from .models import Order, OrderItem
from .forms import OrderForm


# Create your views here.


def create_order(request):
    cart = Cart(request)
    if not len(cart):
        return redirect('cart:cart_detail')
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                )
            cart.clear()
            request.session['order_id'] = order.id
            return redirect(reverse('payments:process'))
    else:
        form = OrderForm()
    context = {'cart': cart, 'form': form}
    return render(request, 'orders/create.html', context)
