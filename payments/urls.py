from django.urls import path
from .views import payment_process, listen_status


app_name = 'payment'


urlpatterns = [
    path('process/', payment_process, name='process'),
    path('listen/', listen_status, name='listen'),
]
