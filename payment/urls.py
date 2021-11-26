from django.urls import path
from .views import *

urlpatterns = [
    path('success/', PaymentSuccessView.as_view(), name='success'),
    path('failed/', PaymentFailedView.as_view(), name='failed'),
    path('history/', OrderHistoryListView.as_view(), name='history'),
    path('import/', importVille, name='importVille'),
    path('api/checkout-session/', create_checkout_session, name='api_checkout_session'),
]