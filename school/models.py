from django.conf import settings
from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """Курс"""
    title = models.CharField(max_length=100, verbose_name='название курса')  # название,
    avatar = models.ImageField(upload_to='media/school', verbose_name='аватар', **NULLABLE)  # превью (картинка),
    description = models.TextField(verbose_name='описание', **NULLABLE)  # описание.
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец курса', **NULLABLE)

    def __str__(self):
        return f'{self.title}' or ''

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    """Урок"""
    title = models.CharField(max_length=100, verbose_name='название урока')  # название урока
    avatar = models.ImageField(upload_to='media/school', verbose_name='аватар', **NULLABLE)  # превью (картинка),
    description = models.TextField(verbose_name='описание', **NULLABLE)  # описание.
    url = models.TextField(verbose_name='ссылка на видео')  # ссылка на видео.
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец урока', **NULLABLE)

    def __str__(self):
        return f'{self.title} {self.url}' or ''

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Subscription(models.Model):
    """ Признак подписки пользователя на курс"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="пользователь")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    subscribed = models.BooleanField(default=False, verbose_name='признак подписки')

    def __str__(self):
        return f'{self.user} - {self.course}' or ''

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
