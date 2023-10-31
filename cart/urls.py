from django.urls import path
from .views import cart_add, cart_remove, cart_clear, cart_detail


app_name = 'cart'


urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', cart_add,name='add'),
    path('remove/<int:product_id>', cart_remove, name='remove'),
    path('remove/all/', cart_clear, name='clear'),
]
