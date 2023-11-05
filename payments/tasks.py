from celery import shared_task
from django.core.mail import send_mail


@shared_task
def payment_succeeded(from_email, to_email):
    theme = 'Оплата товара'
    message = 'Оплата завершена успешно!'
    send_mail(theme, message, from_email, [to_email])
    
    
@shared_task
def payment_canceled(from_email, to_email):
    theme = 'Оплата товара'
    message = 'Оплата была отменена!'
    send_mail(theme, message, from_email, [to_email])