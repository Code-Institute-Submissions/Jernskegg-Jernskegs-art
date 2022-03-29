from django.shortcuts import render, redirect
from .forms import ImageOrderForm, RequestOrderForm

def image_checkout(request):
    cart = request.session.get('cart', [])
    if not cart:
        return (redirect('cart'))

    checkout_cart = cart_contents(request)
    checkout_total = round(checkout_cart['cart_total'] * 100)
    image_order_form = ImageOrderForm()

    context = {
        'image_order_form': image_order_form,
        'stripe_public_key': 'pk_test_51KfDRkIg4lSUQisOn8ULHWmTQqttbloUoKwBA0AxBGITp0ymoI1xS4jHe26JJjm6t7dtcqF9SRaSRQMPqsayphM4003wAyPLMK',
        'client_secret': 'test client secret',
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
