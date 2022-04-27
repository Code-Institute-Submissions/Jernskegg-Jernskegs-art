'''
Checkout view
'''
from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404,
                              HttpResponse)
from django.conf import settings
from django.views.decorators.http import require_POST


from .forms import ImageOrderForm, RequestOrderForm
from cart.contexts import cart_contents
from .models import ImageOrderLineItem, ImageOrderInfo
from gallery.models import ImageEntry

import json
import stripe

# import Stripe keys from settings
stripe_currency = settings.STRIPE_CURRENCY
stripe_public_key = settings.STRIPE_PUBLIC_KEY
stripe_secret_key = settings.STRIPE_SECRET_KEY


@require_POST
def image_checkout_data(request):
    try:
        client_id = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(client_id, metadata={
            'cart': json.dumps(request.session.get('cart', []))
        })
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(content=e, status=400)


def image_checkout(request):
    '''
    this renders the checkout page, the form and the stripe elements.
    '''
    if request.method == 'POST':
        cart = request.session.get('cart', [])

        # Assigning fields for form

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email_address': request.POST['email_address'],
            'phone_number': request.POST['phone_number'],
        }
        image_order_form = ImageOrderForm(form_data)

        # Check if form is valid

        if image_order_form.is_valid():
            image_order = image_order_form.save(commit=False)
            image_order.client_id = request.POST.get(
                'client_secret').split('_secret')[0]
            # Add user id, if user id is 'None' Assign '2' For anon user

            if request.user.id is None:
                image_order.user.id = 2
                image_order.save()
            else:
                image_order.user.id = request.user.id
                image_order.save()

            # Iterate trough items in cart to add them to order as line items

            for item_id in cart:
                try:
                    image_item = ImageEntry.objects.get(id=item_id)
                    image_line_item = ImageOrderLineItem(
                        order=image_order,
                        image_product=image_item,
                    )
                    image_line_item.save()

                # Incase image doesn't exist stop the order and remove it

                except ImageEntry.DoesNotExist:
                    image_order.delete()
                    return redirect('cart')

            return redirect(reverse('checkout_success',
                                    args=[image_order.order_id]))
        else:
            return redirect('cart')

    else:
        cart = request.session.get('cart', [])
        if not cart:
            return (redirect('cart'))

        checkout_cart = cart_contents(request)
        checkout_total = round(checkout_cart['cart_total'] * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=checkout_total,
            currency=stripe_currency,
        )
        image_order_form = ImageOrderForm()

        context = {
            'image_order_form': image_order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, 'checkout.html', context)


def request_checkout(request):
    request_cart = request.session.get('request_cart', [])
    if not request_cart:
        return (redirect('request'))

    request_order_form = RequestOrderForm()

    checkout_cart = cart_contents(request)
    checkout_total = round(checkout_cart['cart_total'] * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=checkout_total,
        currency=stripe_currency,
    )
    context = {
        'request_order_form': request_order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout.html', context)


def checkout_success(request, order_id):
    if 'I-' in order_id:
        checkout_order = get_object_or_404(ImageOrderInfo, order_id=order_id)
    else:
        checkout_order = get_object_or_404(request_checkout, order_id=order_id)

    if 'cart' in request.session:
        del request.session['cart']
    context = {
        'checkout_order': checkout_order,
    }

    return render(request, 'checkout_success.html', context)
