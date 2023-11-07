from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from school.models import Course, Subscription, Lesson
from users.models import User


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.course = Course.objects.create(
            title='TestCourse',
            description='Test',
        )

        self.user = User.objects.create(
            email='admin@mail.ru',
            password='0000',
            is_superuser=True
        )

        self.data = {
            'user': self.user,
            'course': self.course,
        }
        self.subscription = Subscription.objects.create(**self.data)
        self.client.force_authenticate(user=self.user)

    def test_create_subscription(self):
        """Тестирование подписки на курс"""

        data = {
            'user': self.user.pk,
            'course': self.course.pk,
            'subscribed': True
        }

        response = self.client.post(
            reverse('school:subscription-list'),
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Subscription.objects.all().count(),
            2
        )

        self.assertEqual(
            response.json(),
            {
                "id": 2,
                "subscribed": True,
                "user": self.user.pk,
                "course": self.course.pk
            }
        )

    def test_unsubscribe(self):
        """Тестирование отписки на курс"""

        data = {
            'user': self.user.pk,
            'course': self.course.pk,
            'subscribed': False
        }

        response = self.client.patch(
            reverse('school:subscription-detail', kwargs={'id': self.subscription.pk}),
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            Subscription.objects.all().count(),
            1
        )

        self.assertEqual(
            response.json(),
            {
                "id": self.subscription.pk,
                "subscribed": False,
                "user": self.user.pk,
                "course": self.course.pk
            }
        )

    def test_list_subscription(self):
        """Тестирование списка подписок"""

        response = self.client.get(
            reverse('school:subscription-list'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            Subscription.objects.all().count(),
            1
        )

    def test_subscription_retrieve(self):
        """Тестирование вывода одной подписки"""

        response = self.client.get(
            reverse('school:subscription-detail', kwargs={'id': self.subscription.pk})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "id": self.subscription.pk,
                "subscribed": False,
                "user": self.user.pk,
                "course": self.course.pk
            }
        )

    def test_subscription_destroy(self):
        """Тестирование удаления подписки"""

        response = self.client.delete(
            reverse('school:subscription-detail', kwargs={'id': self.subscription.pk})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            list(Subscription.objects.all()),
            []
        )

    def tearDown(self):
        self.user.delete()
        self.course.delete()
        self.subscription.delete()


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.course = Course.objects.create(
            title='TestCourse',
            description='Test'
        )

        self.user = User.objects.create(
            email='admin@mail.ru',
            password='0000',
            is_superuser=True
        )

        self.lesson = Lesson.objects.create(
            course=self.course,
            title='TestLesson',
            description='TestLessonDescription',
            url='https://youtube.com',
            owner=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_create_Lesson(self):
        """Создание урока"""
        data = {
            "course": self.course.pk,
            "title": "TEST1",
            "description": "TEST1",
            "url": "https://youtube.com",
            "owner": self.user.pk
        }

        response = self.client.post(
            reverse('school:lesson-create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 2, 'title': 'TEST1', 'description': 'TEST1', 'avatar': None, 'url': 'https://youtube.com',
             'course': self.course.pk, 'owner': self.user.pk}

        )

        self.assertTrue(
            Lesson.objects.all().count(), 2
        )




    def test_get_list(self):
        response = self.client.get(
            reverse('school:lesson-list')
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_lesson_retrieve(self):
        response = self.client.get(
            reverse('school:lesson-get', kwargs={'pk': self.lesson.pk})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 6, 'title': 'TestLesson', 'description': 'TestLessonDescription', 'avatar': None,
             'url': 'https://youtube.com', 'course': self.course.pk, 'owner': self.user.pk}

        )

    def test_lesson_update(self):
        data = {
            "course": self.course.pk,
            "title": "LessonTestTitle",
            "description": "TEST2",
            "url": "https://youtube.com/testtest/",
            "owner": self.user.pk
        }

        response = self.client.patch(
            reverse('school:lesson-update', kwargs={'pk': self.lesson.pk}),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 7, 'title': 'LessonTestTitle', 'description': 'TEST2', 'avatar': None,
             'url': 'https://youtube.com/testtest/', 'course': self.course.pk, 'owner': self.user.pk}

        )

    def test_lesson_destroy(self):
        response = self.client.delete(
            reverse('school:lesson-delete', kwargs={'pk': self.lesson.pk})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            list(Lesson.objects.all()),
            []
        )
    def test_create_bad_Lesson(self):
        """Создание урока с ошибкой"""
        data = {
            "course": self.course.pk,
            "title": "TEST3",
            "description": "TEST3",
            "url": "https://google.com",
            "owner": self.user.pk
        }

        response = self.client.post(
            reverse('school:lesson-create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
    def tearDown(self):
        self.user.delete()
        self.course.delete()
        self.lesson.delete()
