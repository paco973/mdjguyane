from django.db import models
from django.core import validators

from store.models import Cart


class OrderDetail(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )

    identifiant = models.CharField(
        max_length=100,
        null=True,
    )

    # You can change as a Foreign Key to the user model
    customer_email = models.EmailField(
        verbose_name='Customer Email'
    )

    amount = models.IntegerField(
        verbose_name='Amount'
    )

    stripe_payment_intent = models.CharField(
        max_length=200
    )

    # This field can be changed as status
    has_paid = models.BooleanField(
        default=False,
        verbose_name='Payment Status'
    )

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.customer_email
