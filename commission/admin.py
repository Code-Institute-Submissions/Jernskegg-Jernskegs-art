''' Model to admin panel '''
from django.contrib import admin
from .models import Genre, CommissionRequest, Comment


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['comment_posted_by']


class CommissionRequestAdmin(admin.ModelAdmin):
    search_fields = ['title']


class GenreAdmin(admin.ModelAdmin):
    search_fields = ['title'],
    list_display = ('title', 'price')


admin.site.register(Genre, GenreAdmin)
admin.site.register(CommissionRequest, CommissionRequestAdmin)
admin.site.register(Comment, CommentAdmin)
