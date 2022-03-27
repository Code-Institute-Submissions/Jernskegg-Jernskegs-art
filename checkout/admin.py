from django.contrib import admin
from .models import ImageOrderInfo, ImageOrderLineItem

# Register your models here.

class ImageOrderLineAdmin(admin.TabularInline):
    model = ImageOrderLineItem
    readonly_fields = ('image_lineitem_total',)

class ImageOrderAdmin(admin.ModelAdmin):
    inlines = (ImageOrderLineAdmin,)

    readonly_fields = ('order_id', 'date_ordered', 'order_total',)

    fields = (
        'order_id',
        'first_name',
        'last_name',
        'email_address',
        'date_ordered',
        'phone_number',
        'order_total',
        )

    list_display = ('order_id', 'date_ordered', 'first_name', 'last_name', 'order_total')

    ordering = ('-date_ordered',)
2
admin.site.register(ImageOrderInfo, ImageOrderAdmin)
