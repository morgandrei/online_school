from datetime import datetime
from django.core.management.base import BaseCommand
from payment.models import Payment
from users.models import User
from school.models import Lesson, Course
from decimal import Decimal
import random


class Command(BaseCommand):

     def handle(self, *args, **kwargs):
        users = User.objects.all()
        courses = Course.objects.all()
        lessons = Lesson.objects.all()

        for user in users:
            payment = Payment(
                user=user,
                pay_date=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                pay_course=random.choice(courses) if courses else None,
                pay_lesson=random.choice(lessons) if lessons else None,
                prise=Decimal(random.uniform(10, 2000)),
                pay_method=random.choice([Payment.PAYMENT_CHOICES[0], Payment.PAYMENT_CHOICES[1]])
            )
            payment.save()
