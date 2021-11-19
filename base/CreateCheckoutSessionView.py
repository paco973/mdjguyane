import stripe
from django.conf import settings
from django.shortcuts import redirect
from django.views import View

stripe.api_key = settings.STRIPE_PUBLIC_KEY
YOUR_DOMAIN = 'http://127.0.0.1:8000'


class CreateCheckoutSessionView(View):

    def post(self, request, *args, **kwargs):
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (e.g. pr_1234) of the product you want to sell
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
                },
            ],
            payment_method_types=[
                'card',
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )

        return redirect(checkout_session.url, code=303)
