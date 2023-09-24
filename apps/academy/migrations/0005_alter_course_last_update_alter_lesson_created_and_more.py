# Generated by Django 4.2.5 on 2023-09-23 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0004_course_last_update_lesson_created_lesson_last_update_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='last_update',
            field=models.DateTimeField(auto_now=True, verbose_name='last updated'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='last_update',
            field=models.DateTimeField(auto_now=True, verbose_name='last upload at'),
        ),
    ]