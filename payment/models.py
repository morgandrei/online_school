from django.db import models

from school.models import Course, Lesson
from users.models import User, NULLABLE


class Payment(models.Model):
    """Платежи"""

    PAYMENT_CHOICES = [
        ('cash', 'Наличные'),
        ('card', 'Перевод'),
    ]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='плательщик', **NULLABLE)  # пользователь
    pay_date = models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')  # дата оплаты,
    pay_course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='оплаченный курс', **NULLABLE)
    pay_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='оплаченный урок', **NULLABLE)
    prise = models.FloatField(verbose_name='сумма оплаты', )  # сумма оплаты,
    pay_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.user} - {self.pay_course if self.pay_course else self.pay_lesson}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
