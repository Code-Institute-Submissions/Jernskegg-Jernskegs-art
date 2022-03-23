''' Account view models '''
from django.views import generic
from django.shortcuts import render
from commission.models import CommissionRequest

# Create your views here.


class GetAccount(generic.ListView):
    ''' Account page view '''
    model = CommissionRequest
    context_object_name = 'commission'
    template_name = 'account.html'
