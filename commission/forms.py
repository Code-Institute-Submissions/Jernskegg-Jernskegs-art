from .models import CommissionRequest
from django import forms


class AddCommissionRequest(forms.ModelForm):
    class Meta:
        model = CommissionRequest
        fields = ('type', 'image_size', 'user_description')
