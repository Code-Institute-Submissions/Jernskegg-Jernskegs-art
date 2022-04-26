from django.urls import path
from . import views
from commission.views import archive_request

urlpatterns = [
    path('', views.GetAccount.as_view(), name='account'),
    path('delete/<item_id>', archive_request, name='delete_request')
]
