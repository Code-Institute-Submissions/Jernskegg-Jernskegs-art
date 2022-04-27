from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError

from datetime import date

from gallery.models import ImageEntry
from checkout.models import ImageOrderInfo, RequestOrderInfo
from simple_pages.models import Contact
from commission.models import CommissionRequest

from .forms import UpdateProductForm, AddNewProduct
# Create your views here.


def get_admin_panel_overview(request):
    ''' just returns the admin_panel.html '''

    context = {
        'switch': 'overview',
        'date': date.today(),
        'images': ImageEntry.objects.all(),
        'image_order': ImageOrderInfo.objects.all(),
        'request_order': RequestOrderInfo.objects.all(),
        'commission': CommissionRequest.objects.all(),
        'contact': Contact.objects.all(),
    }
    return render(request, 'overview.html', context)


def get_admin_panel_requests(request):
    ''' just returns the admin_panel.html '''
    context = {
        'switch': 'requestList',
        'date': date.today(),
        'request_order': RequestOrderInfo.objects.all(),
        'commission': CommissionRequest.objects.all(),
    }
    return render(request, 'requests.html', context)


def get_admin_panel_purchase_history(request):
    ''' just returns the admin_panel.html '''
    context = {
        'switch': 'purchaseHistory',
        'date': date.today(),
        'image_order': ImageOrderInfo.objects.all(),
    }
    return render(request, 'purchases.html', context)


def get_admin_panel_contact_inquiries(request):
    ''' just returns the admin_panel.html '''
    context = {
        'switch': 'contactInquiries',
        'date': date.today(),
        'contact': Contact.objects.all(),
    }
    return render(request, 'contacts.html', context)


def get_admin_panel_products(request, switch='overview'):
    ''' just returns the admin_panel.html '''

    context = {
        'switch': 'products',
        'date': date.today(),
        'images': ImageEntry.objects.all(),
    }
    return render(request, 'products.html', context)


def update_product(request, item_id):
    '''
    Update the selected product
    '''
    product = ImageEntry.objects.get(id=item_id)
    try:
        request.POST['hide_me']
        hidden = True
    except MultiValueDictKeyError:
        hidden = False
    except Exception:
        return redirect(get_admin_panel_products)

    form_data = {
        'hidden': hidden,
        'price': request.POST['price'],
    }
    update_product_form = UpdateProductForm(form_data)

    if update_product_form.is_valid():
        print('valid')
        product.price = request.POST['price']
        print(hidden)
        product.hidden = hidden
        product.save()
        return redirect(get_admin_panel_products)


def check_file_format(files=''):
    check_file = str(files)
    check_string = check_file.split()
    both_files_correct = 0  # get this to 2
    for x in check_string:
        if 'image/' in x:
            both_files_correct += 1

    if both_files_correct == 2:
        return True
    else:
        return False


def add_new_product(request, error=''):
    setform = AddNewProduct

    if request.method == 'POST':
        form = setform(request.POST, request.FILES)
        if check_file_format(request.FILES):
            if form.is_valid():
                new_product = form.save(commit=False)
                new_product.save()
                return redirect(get_admin_panel_products)

    else:
        form = AddNewProduct
    context = {
        'error_message': error,
        'switch': 'products',
        'form': form,
    }
    return render(request, 'products_add.html', context)


def remove_product(request, item_id):
    delete_product = get_object_or_404(ImageEntry, id=item_id)
    delete_product.delete()
    return redirect(get_admin_panel_products)
