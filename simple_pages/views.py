''' Views to show just html templates '''
from django.shortcuts import render, redirect
from django.views import generic
from gallery.models import ImageEntry
from .forms import AddContactQuery, AddNewsletter

# Create your views here.


class GetHome(generic.ListView):
    '''
    Class based view to render the model to index
    template paginated to only show the 4 newest ones
    '''
    model = ImageEntry
    context_object_name = 'images'
    template_name = 'index.html'
    paginate_by = 4


def get_about(request):
    ''' just returns the about.html '''
    return render(request, 'about.html')


def get_contact(request):
    '''
    function to handle contact inqueries
    '''
    contact_form = AddContactQuery

    if request.method == 'POST':
        form = contact_form(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddContactQuery
    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)


def sign_newsleter(request):
    if request.method == 'POST':
        if 'newsletter-email' in request.POST:
            form = AddNewsletter
            form.email_address = request.POST['newsletter-email']
            if form.is_valid():
                form.save()
                return redirect('home')
