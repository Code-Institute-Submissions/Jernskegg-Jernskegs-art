''' Model to admin panel '''
from django.contrib import admin
from .models import ImageEntry


class ImageEntryAdmin(admin.ModelAdmin):

    list_display = ('title', 'date_posted', 'is_hidden', 'price')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'image']
    list_filter = ('date_posted', 'price', 'is_hidden')
    list_editable = ('is_hidden',)


admin.site.register(ImageEntry, ImageEntryAdmin)
