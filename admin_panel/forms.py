from django import forms
from gallery.models import ImageEntry


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = ImageEntry
        fields = (
            'hidden',
            'price',
        )