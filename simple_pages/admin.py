from django.contrib import admin
from .models import Newsletter, Contact

# Register your models here.


class NewsletterAdmin(admin.ModelAdmin):
    fields = (
        'email_address',
    )


class ContactAdmin(admin.ModelAdmin):

    fields = (
        'first_name',
        'last_name',
        'email_address',
        'date_ordered',
        )

    list_display = (
        'first_name',
        'last_name',
        )

    search_fields = ['email_address', ]
    list_filter = ('date_contacted', 'email_address',)

    ordering = ('-date_contacted',)


admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Contact, ContactAdmin)
