from django.views import generic
from commission.models import CommissionRequest

# Create your views here.


class GetAccount(generic.ListView):
    model = CommissionRequest
    context_object_name = 'commission'
    template_name = 'account.html'
