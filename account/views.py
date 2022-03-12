from django.shortcuts import render

# Create your views here.
def get_account(request):
    return render(request, 'account.html')