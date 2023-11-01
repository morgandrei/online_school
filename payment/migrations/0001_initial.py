# Generated by Django 4.2.6 on 2023-11-01 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0002_course_les_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_date', models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')),
                ('prise', models.FloatField(verbose_name='сумма оплаты')),
                ('pay_method', models.CharField(choices=[('cash', 'Наличные'), ('card', 'Перевод')], max_length=20, verbose_name='способ оплаты')),
                ('pay_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.course', verbose_name='оплаченный курс')),
                ('pay_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.lesson', verbose_name='оплаченный урок')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='плательщик')),
            ],
            options={
                'verbose_name': 'платеж',
                'verbose_name_plural': 'платежи',
            },
        ),
    ]
