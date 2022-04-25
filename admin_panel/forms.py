from django import forms
from gallery.models import ImageEntry


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = ImageEntry
        fields = (
            'is_hidden',
            'price',
        )


class AddNewProduct(forms.ModelForm):
    class Meta:
        model = ImageEntry
        fields = {
            'title',
            'image',
            'water_marked_image',
            'price',
            'is_hidden',
        }
