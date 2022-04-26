from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetHome.as_view(), name='home'),
    path('about/', views.get_about, name='about'),
    path('contact/', views.get_contact, name='contact'),
    path('newsletter', views.sign_newsleter, name='add_to_newsletter'),
]
