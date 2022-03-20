''' Views to show just html templates '''
from django.shortcuts import render

# Create your views here.


def get_home(request):
    return render(request, 'index.html')


def get_about(request):
    return render(request, 'about.html')
