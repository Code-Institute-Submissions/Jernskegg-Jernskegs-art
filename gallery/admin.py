from django.contrib import admin
from .models import imageEntry


class imageEntry_admin(admin.ModelAdmin):

    list_display = ('title', 'date_posted', 'price')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'image']
    list_filter = ('date_posted','price' )



admin.site.register(imageEntry, imageEntry_admin)