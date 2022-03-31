from django.http import HttpResponse
from django.conf import settings
from .webhook_handler import StripeWH_Handler
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

import stripe

# Using Django


@require_POST
@csrf_exempt
def webhook(request):
    '''Stripe webook listener'''
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
            )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(content=e, status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(content=e, status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Webhook handler
    handler = StripeWH_Handler(request)

    # event webhook map
    event_map = {
        'payment_intent.succeeded':
        handler.handle_payment_intent_succeeded,

        'payment_intent.payment_failed':
        handler.handle_payment_intent_payment_failed,
    }

    # get event type from Stripe
    event_type = event['type']

    # if handler exist get it from event map else use default
    event_handler = event_map.get(event_type, handler.handle_event)

    # event handler response
    response = event_handler(event)
    return response
