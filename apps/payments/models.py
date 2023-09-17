from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.academy.models import Course, Lesson
from apps.users.models import User, NULLABLE


class Payment(models.Model):
    class MethodPayment(models.TextChoices):
        cash = ('cash', _('cash'))
        card_transfer = ('card_transfer', _('card transfer'))

    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('amount'))
    method_payment = models.CharField(choices=MethodPayment.choices, verbose_name=_('method payment'))
    datetime_payment = models.DateTimeField(auto_now=True, verbose_name=_('datetime payment'))

    creator = models.ForeignKey(
        to=User, related_name='payments', on_delete=models.DO_NOTHING, verbose_name=_('user')
    )
    course_payment = models.ForeignKey(
        to=Course, **NULLABLE, related_name='payments', on_delete=models.DO_NOTHING, verbose_name=_('course payment')
    )
    lesson_payment = models.ForeignKey(
        to=Lesson, **NULLABLE, related_name='payments', on_delete=models.DO_NOTHING, verbose_name=_('lesson payment')
    )

    def __str__(self):
        if self.course_payment:
            return f'{self.creator.email} {self.course_payment} {self.amount}'
        elif self.lesson_payment:
            return f'{self.creator.email} {self.lesson_payment} {self.amount}'
        return f'{self.creator.email}'

    class Meta:
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')
