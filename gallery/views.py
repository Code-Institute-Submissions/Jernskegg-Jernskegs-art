'''Django view file'''
from django.views import generic
from gallery.models import ImageEntry


class ImageList(generic.ListView):
    '''
    Class based view to render the model to gallery template
    '''
    model = ImageEntry
    context_object_name = 'images'
    queryset = ImageEntry.objects.order_by('-date_posted')
    template_name = 'gallery.html'
