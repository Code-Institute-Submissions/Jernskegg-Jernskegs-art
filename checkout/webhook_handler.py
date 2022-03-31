from django.http import HttpResponse
from .models import ImageOrderInfo, ImageOrderLineItem
from gallery.models import ImageEntry

import json
import time


class StripeWH_Handler:
    ''' Class that handles stripe webhook'''

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        '''
        Generic/Uknown/Unexpected Webhook event
        '''
        return HttpResponse(
            content=f'unhandled webhook recieved: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        '''
        Generic/Uknown/Unexpected Webhook event
        '''
        intent = event.data.object
        client_id = intent.id
        cart = intent.metadata.cart

        billing_details = intent.charges.data[0].billing_details
        total = round(intent.charges.data[0].amount / 100, 2)

        order_in_database = False
        # Tries to match order items in the database,
        # if not found make a database entry
        attempt = 1
        while attempt <= 5:
            try:
                image_order = ImageOrderInfo.objects.get(
                    first_name__iexact=billing_details.name.split(' ')[0],
                    last_name__iexact=billing_details.name.split(' ')[1],
                    email_address__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    order_total=total,
                    client_id=client_id,
                )
                order_in_database = True
                break
            except ImageOrderInfo.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_in_database:
            return HttpResponse(
                content=f'Webhook recieved: {event["type"]} | SUCCESS: Order allready in database,\
nofurther action required',
                status=200
            )
        else:
            # If datase didn't match we create a entry here
            image_order = None
            try:
                image_order = ImageOrderInfo.objects.create(
                    first_name=billing_details.name.split(' ')[0],
                    last_name=billing_details.name.split(' ')[1],
                    email_address=billing_details.email,
                    phone_number=billing_details.phone,
                    client_id=client_id,
                    )

                for item_id in json.loads(cart):
                    try:
                        image_item = ImageEntry.objects.get(id=item_id)
                        image_line_item = ImageOrderLineItem(
                            order=image_order,
                            image_product=image_item,
                        )

                        image_line_item.save()
                    except ImageEntry.DoesNotExist:
                        image_order.delete()
            except Exception as e:
                if image_order:
                    image_order.delete()
                return HttpResponse(
                    content=f'Webhook recieved: {event["type"]} | ERROR {e}',
                    status=500
                    )

        return HttpResponse(
            content=f'''Webhook recieved: {event["type"]} \
| SUCCESS: Created Image order in webhook''',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        '''
        Generic/Uknown/Unexpected Webhook event
        '''
        return HttpResponse(
            content=f'Payment Failed Webhook recieved: {event["type"]}',
            status=200
        )
