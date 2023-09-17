from django.urls import path

from apps.payments.apps import PaymentsConfig
from apps.payments.views import PaymentListAPIView

app_name = PaymentsConfig.name

urlpatterns = [
    path('api/payment/', PaymentListAPIView.as_view(), name='api_payment_list')
]
