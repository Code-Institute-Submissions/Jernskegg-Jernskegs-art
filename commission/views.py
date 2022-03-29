from django.shortcuts import render, redirect
from .forms import AddCommissionRequest

# Create your views here.


def add_request(request):
    request_cart = request.session.get('request_cart', [])
    setform = AddCommissionRequest

    if request_cart != []:
        request.session.pop('request_cart')

    if request.method == 'POST':
        form = setform(request.POST or None)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.requested_by = request.user
            new_request.save()

            request_cart.append(new_request.id)
            print(request_cart)
            request.session['request_cart'] = request_cart

            return redirect('request_checkout')
    else:
        form = AddCommissionRequest
    context = {
        'form': form,
    }
    return render(request, 'request.html', context)
