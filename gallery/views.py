from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from gallery.models import imageEntry

class imageList(generic.ListView):
    model = imageEntry
    context_object_name = 'images'
    queryset = imageEntry.objects.order_by('-date_posted')
    template_name = 'gallery.html'
