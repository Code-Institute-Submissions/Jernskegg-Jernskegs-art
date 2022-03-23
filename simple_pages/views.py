''' Views to show just html templates '''
from django.shortcuts import render

# Create your views here.


def get_home(request):
    ''' just returns the index.html '''
    return render(request, 'index.html')


def get_about(request):
    ''' just returns the about.html '''
    return render(request, 'about.html')
