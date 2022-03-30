from django.http import HttpResponse


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
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
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
