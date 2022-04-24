from django.shortcuts import render, HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from datetime import date

from gallery.models import ImageEntry
from checkout.models import ImageOrderInfo, RequestOrderInfo
from simple_pages.models import Contact
from commission.models import CommissionRequest

from .forms import UpdateProductForm

# Create your views here.


def get_admin_panel(request):
    ''' just returns the admin_panel.html '''
    time = date.today()

    context = {
        'date': time,
        'images': ImageEntry.objects.all(),
        'image_order': ImageOrderInfo.objects.all(),
        'request_order': RequestOrderInfo.objects.all(),
        'commission': CommissionRequest.objects.all(),
        'contact': Contact.objects.all(),
    }
    return render(request, 'admin_panel.html', context)


def update_product(request, item_id):
    '''
    Update the selected product
    '''
    product = ImageEntry.objects.get(id=item_id)
    try:
        request.POST['hidden']
        hidden = True
    except MultiValueDictKeyError:
        hidden = False

    form_data = {
        'hidden': hidden,
        'price': request.POST['price'],
    }
    update_product_form = UpdateProductForm(form_data)

    if update_product_form.is_valid():
        product.price = request.POST['price']
        product.hidden = hidden
        product.save()
        get_admin_panel()