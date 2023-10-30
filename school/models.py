from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    """Курс"""
    title = models.CharField(max_length=100, verbose_name='название курса')  # название,
    avatar = models.ImageField(upload_to='media/school', verbose_name='аватар', **NULLABLE)  # превью (картинка),
    description = models.TextField(verbose_name='описание', **NULLABLE)  # описание.

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

    def __str__(self):
        return f'{self.title} {self.url}' or ''

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
