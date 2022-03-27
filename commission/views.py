from django.shortcuts import render, redirect
from .forms import AddCommissionRequest

# Create your views here.


def add_request(request):
    setform = AddCommissionRequest
    if request.method == 'POST':
        form = setform(request.POST or None)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.requested_by = request.user
            new_request.save()
            return redirect('/accounts/')
    else:
        form = AddCommissionRequest
    context = {
        'form': form,
    }
    return render(request, 'request.html', context)
