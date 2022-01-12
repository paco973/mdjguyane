from django.http.response import HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from base.models import MdjMember, City, Student
from store.views import _cart_id
from .models import *
from django.views.generic import ListView, TemplateView
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

@csrf_exempt
def create_checkout_session(request):
    request_data = json.loads(request.body)

    stripe.api_key = settings.STRIPE_SECRET_KEY
    if len(request_data) > 1:
        try:
            user = MdjMember.objects.get(indentifiant=request_data['email'])
        except:
            return JsonResponse({'message': "paco"})
        try:
            order_verification = OrderDetail.objects.get(
                indentifiant=request_data['email'],
                cart_id=_cart_id(request),
                has_paid=False
            )
            message = 2
        except:
            pass
            # return JsonResponse({'message': "paco"})

        checkout_session = stripe.checkout.Session.create(
            # Customer Email is optional,
            # It is not safe to accept email directly from the client side
            customer_email=user.email,
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {
                            'name': 'Panier Solidaire',
                        },
                        'unit_amount': int(6 * 100),
                    },
                    'quantity': 1,
                }
            ],
            mode='payment',

            success_url=request.build_absolute_uri(
                reverse('success')
            ) + "?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=request.build_absolute_uri(reverse('failed')),
        )

        # OrderDetail.objects.create(
        #     customer_email=email,
        #     product=product, ......
        # )

        order = OrderDetail()
        order.cart = Cart.objects.get(cart_id=_cart_id(request))
        order.customer_email = user.email
        order.stripe_payment_intent = checkout_session['payment_intent']
        order.amount = int(6 * 100)
        order.save()
    else:

        try:
            member = MdjMember.objects.get(email=request_data['email'])
        except:
            return redirect('member')

        checkout_session = stripe.checkout.Session.create(
            # Customer Email is optional,
            # It is not safe to accept email directly from the client side
            customer_email=request_data['email'],
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {
                            'name': member.role.name,
                        },
                        'unit_amount': int(member.role.nombre * 100),
                    },
                    'quantity': 1,
                }
            ],
            mode='payment',

            success_url=request.build_absolute_uri(
                reverse('success')
            ) + "?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=request.build_absolute_uri(reverse('failed')),
        )

        # OrderDetail.objects.create(
        #     customer_email=email,
        #     product=product, ......
        # )

        order = OrderDetail()
        order.customer_email = request_data['email']
        order.stripe_payment_intent = checkout_session['payment_intent']
        order.amount = int(6 * 100)
        order.save()

    # return JsonResponse({'data': checkout_session})
    return JsonResponse({'sessionId': checkout_session.id})


class PaymentSuccessView(TemplateView):
    template_name = "payments/payment_success.html"

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')
        if session_id is None:
            return HttpResponseNotFound()

        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.retrieve(session_id)

        order = get_object_or_404(OrderDetail, stripe_payment_intent=session.payment_intent)
        member = MdjMember.objects.get(email=order.customer_email)
        member.active = True
        member.save()
        order.has_paid = True
        order.save()
        return render(request, self.template_name)


class PaymentFailedView(TemplateView):
    template_name = "payments/payment_failed.html"


class OrderHistoryListView(ListView):
    model = OrderDetail
    template_name = "payments/order_history.html"


def importVille(request):
    with open('./correspondance-code-insee-code-postal.json') as json_data:
        datas = json.load(json_data)
    json_data.close()

    for data in datas:
        ville = City.objects.create(name=data["fields"]["nom_comm"],
                                    description=data["fields"]["statut"] + " " + data["fields"]["nom_region"])
        ville.save()

    return redirect('home')
