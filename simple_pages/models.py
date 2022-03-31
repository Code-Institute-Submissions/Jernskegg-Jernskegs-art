from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=64, null=False, blank=False)
    last_name = models.CharField(max_length=64, null=False, blank=False)
    date_contacted = models.DateField(auto_now_add=True, editable=False)
    email_address = models.EmailField(max_length=255, null=False,)
    phone_number = models.CharField(max_length=15)
    query = models.TextField(max_length=255)

    def __str__(self):
        return f'{self.first_name} asked {self.query}'


class Newsletter(models.Model):
    email_address = models.EmailField(max_length=255, null=False,)
