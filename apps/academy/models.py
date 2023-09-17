from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.users.models import NULLABLE, User


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    description = models.TextField(**NULLABLE, verbose_name=_('description'))
    preview = models.ImageField(**NULLABLE, upload_to='courses/previews', verbose_name=_('preview'))

    creator = models.ForeignKey(
        User, related_name='courses', on_delete=models.DO_NOTHING, verbose_name=_('course creator')
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    description = models.TextField(**NULLABLE, verbose_name=_('description'))
    video_link = models.CharField(**NULLABLE, max_length=255, verbose_name=_('video link'))
    preview = models.ImageField(**NULLABLE, upload_to='lessons/previews', verbose_name=_('preview'))

    course = models.ForeignKey(
        Course, related_name='lessons', on_delete=models.DO_NOTHING, verbose_name=_('course')
    )
    creator = models.ForeignKey(
        User, related_name='lessons', on_delete=models.DO_NOTHING, verbose_name=_('lesson creator')
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')
