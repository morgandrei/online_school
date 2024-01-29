from celery import shared_task
from django.contrib.auth.models import User
from django.utils import timezone


@shared_task
def blocking_inactive_users():
    threshold = timezone.now() - timezone.timedelta(days=30)
    User.objects.filter(last_login__lt=threshold, is_active=True).update(is_active=False)
