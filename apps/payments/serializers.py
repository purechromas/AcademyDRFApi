from rest_framework import serializers

from apps.payments.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('user', 'course_payment', 'lesson_payment', 'amount', 'method_payment', 'datetime_payment')