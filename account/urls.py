from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetAccount.as_view(), name='account'),

]
