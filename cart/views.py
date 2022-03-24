'''Create your views here.'''
from django.shortcuts import render


def get_cart(request):
    ''' A view that will enable viewing the shopping cart '''
    return render(request, 'cart.html')
