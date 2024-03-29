from celery import shared_task
from django.core.mail import send_mail
from config import settings
from school.models import Subscription, Course


@shared_task
def send_subscription_notification(course_id):
    course = Course.objects.get(id=course_id)
    subscribers = Subscription.objects.filter(course=course, subscribed=True)
    recipient_list = [s.user.email for s in subscribers]
    send_mail(
            subject='Уведомление об обновлении',
            message=f'В курс {course.title} был добавлен урок.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=recipient_list,
            fail_silently=False,
        )
