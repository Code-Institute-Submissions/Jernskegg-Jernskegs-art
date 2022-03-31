from .models import Contact, Newsletter
from django import forms


class AddContactQuery(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'email_address',
            'phone_number',
            'query',
            )


class AddNewsletter(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = (
            'email_address',
        )
