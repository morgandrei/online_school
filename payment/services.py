import stripe
from django.conf import settings


def create_payment():
    stripe.api_key = settings.STRIPE_KEY
    intent = stripe.PaymentIntent.create(
        amount=2000,
        currency="usd",
        automatic_payment_methods={"enabled": True},
    )
    return intent
