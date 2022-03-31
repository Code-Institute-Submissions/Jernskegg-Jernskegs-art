'''Create your views here.'''
from django.shortcuts import render, redirect, reverse


def get_cart(request):
    ''' A view that will enable viewing the shopping cart '''
    return render(request, 'cart.html')


def add_to_cart(request, item_id):
    ''' Adds an item to the cart'''

    cart = request.session.get('cart', [])

    if int(item_id) not in cart:
        cart.append(int(item_id))
        request.session['cart'] = cart
        return redirect('gallery')
    else:
        return redirect('gallery')


def remove_from_cart(request, item_id):
    ''' Adds an item to the cart'''

    cart = request.session.get('cart', [])
    cart.remove(int(item_id))
    request.session['cart'] = cart
    return redirect(reverse(get_cart))
