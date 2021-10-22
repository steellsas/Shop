from django.urls import path
from .views import payment_done,  payment_canceled, payment_config


app_name = 'payment'

urlpatterns = [
    path('proccess/', payment_config, name='process'),
    path('done/', payment_done, name='done'),
    path('canceled/', payment_canceled, name='canceled'),
]