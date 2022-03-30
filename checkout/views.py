from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import ImageOrderForm, RequestOrderForm
import stripe
from cart.contexts import cart_contents
from django.conf import settings
from .models import ImageOrderLineItem, ImageOrderInfo, RequestOrderInfo
from gallery.models import ImageEntry

# import Stripe keys from settings
stripe_currency = settings.STRIPE_CURRENCY
stripe_public_key = settings.STRIPE_PUBLIC_KEY
stripe_secret_key = settings.STRIPE_SECRET_KEY


def image_checkout(request):
    '''
    this renders the checkout page
    '''
    if request.method == 'POST':
        cart = request.session.get('cart', [])
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email_address': request.POST['email_address'],
            'phone_number': request.POST['phone_number'],
        }
        image_order_form = ImageOrderForm(form_data)
        if image_order_form.is_valid():
            image_order = image_order_form.save(commit=False)
            if request.user.id is None:
                image_order.user.id = 2
                image_order.save()
            else:
                image_order.user.id = request.user.id
                image_order.save()
            for item_id in cart:
                try:
                    image_item = ImageEntry.objects.get(id=item_id)
                    image_line_item = ImageOrderLineItem(
                        order=image_order,
                        image_product=image_item,
                    )
                    image_line_item.save()
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
