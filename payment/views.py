from django.shortcuts import render
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from payment.models import Payment
from payment.serializers import PaymentSerializer


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    filter_backends = [ OrderingFilter, DjangoFilterBackend]
    ordering_fields = ('pay_date',)
    filterset_fields = ('pay_course', 'pay_lesson', 'pay_method')
