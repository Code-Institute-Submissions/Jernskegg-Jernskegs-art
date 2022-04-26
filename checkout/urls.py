from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.image_checkout, name='checkout'),
    path('wh/', webhook, name='webhook'),

    path(
        'success/<order_id>',
        views.checkout_success,
        name='checkout_success',
        ),

    path(
        'image_checkout_data/',
        views.image_checkout_data,
        name='image_checkout_data'
        ),
]
