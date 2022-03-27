''' A context proccesor for the cart '''
from django.shortcuts import get_object_or_404
from gallery.models import ImageEntry


def cart_contents(request):
    ''' Context for cart'''
    cart_items = []
    cart_total = 0
    cart = request.session.get('cart', [])

    for item_id in cart:
        gallery_item = get_object_or_404(ImageEntry, pk=item_id)
        cart_total += gallery_item.price
        cart_items.append({
            'item_id': item_id,
            'gallery_item': gallery_item,
        })

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
    }
    return context
