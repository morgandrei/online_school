from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    """Представление ролей"""
    MEMBER = 'member', _('пользователь')
    MODERATOR = 'moderator', _('модератор')


class User(AbstractUser):
    """Пользователи"""

    username = None
    first_name = models.CharField(max_length=100, verbose_name='имя', **NULLABLE)
    last_name = models.CharField(max_length=100, verbose_name='фамилия', **NULLABLE)
    email = models.EmailField(max_length=100, verbose_name='почта', unique=True)
    avatar = models.ImageField(upload_to='users', default='default.png', **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    about_me = models.TextField(verbose_name='о себе', **NULLABLE)
    token = models.CharField(max_length=100, **NULLABLE)
    is_active = models.BooleanField(default=False)
    role = models.CharField(max_length=15, choices=UserRoles.choices, default=UserRoles.MEMBER,
                            verbose_name='роль в проекте')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}' or ''



    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
