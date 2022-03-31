'''Django view file'''
from django.views import generic
from gallery.models import ImageEntry


class ImageList(generic.ListView):
    '''
    Class based view to render the model to gallery template
    '''
    model = ImageEntry
    context_object_name = 'images'
    template_name = 'gallery.html'

    def get_queryset(self):
        if self.request.GET.get('sort'):
            if 'price' in self.request.GET.get('sort'):
                queryset = super().get_queryset()
                return queryset.order_by('price')
            elif 'name' in self.request.GET.get('sort'):
                queryset = super().get_queryset()
                return queryset.order_by('title')
        else:
            queryset = super().get_queryset()
            return queryset.order_by('-date_posted')
