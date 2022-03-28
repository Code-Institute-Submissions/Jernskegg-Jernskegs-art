from django.shortcuts import render, redirect
from .forms import ImageOrderForm, RequestOrderForm


def image_checkout(request):
    cart = request.session.get('cart', [])
    if not cart:
        return (redirect('cart'))

    image_order_form = ImageOrderForm()

    context = {
        'image_order_form': image_order_form,
    }

    return render(request, 'checkout.html', context)


def request_checkout(request):
    request_cart = request.session.get('request_cart', [])
    if not request_cart:
        return (redirect('request'))

    request_order_form = RequestOrderForm()

    context = {
        'request_order_form': request_order_form,
    }

    return render(request, 'checkout.html', context)
