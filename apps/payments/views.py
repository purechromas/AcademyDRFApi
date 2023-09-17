from rest_framework import generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from apps.payments.models import Payment
from apps.payments.serializers import PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['method_payment', 'course_payment', 'lesson_payment']
    ordering_fields = ['datetime_payment']