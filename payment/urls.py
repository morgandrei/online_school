from django.urls import path
from payment.apps import PaymentConfig
from payment.views import PaymentCreateAPIView, PaymentListAPIView

app_name = PaymentConfig.name


urlpatterns = [
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('', PaymentListAPIView.as_view(), name='payment-list'),
]
