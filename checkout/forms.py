from django import forms
from .models import ImageOrderInfo, RequestOrderInfo


class ImageOrderForm(forms.ModelForm):
    class Meta:
        model = ImageOrderInfo
        fields = (
            'first_name',
            'last_name',
            'email_address',
            'phone_number',
            )


class RequestOrderForm(forms.ModelForm):
    class Meta:
        model = RequestOrderInfo
        fields = (
            'first_name',
            'last_name',
            'email_address',
            'phone_number',
            )
