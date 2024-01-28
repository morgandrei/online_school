from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from school.models import Course, Lesson, Subscription
from school.permissions import IsOwner, IsModerator, IsMember, IsSuperuser
from school.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from school.task import send_subscription_notification
from users.models import UserRoles
from school.pagination import SchoolPagination


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с курсом"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = SchoolPagination

    @action(detail=False, methods=['post'])
    def custom_create(self, request, *args, **kwargs):
        if request.user.role == UserRoles.MODERATOR:
            return Response({"detail": "Модераторы не могут создавать курсы."})
        return super().create(request, *args, **kwargs)

    def custom_destroy(self, request, *args, **kwargs):
        if request.user.role == UserRoles.MODERATOR:
            return Response({"detail": "Модераторы не могут удалять курсы."})
        return super().destroy(request, *args, **kwargs)


class LessonCreateAPIView(generics.CreateAPIView):
    """Создание урока"""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsMember | IsSuperuser]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()

        send_subscription_notification.delay(new_lesson.course)


class LessonListAPIView(generics.ListAPIView):
    """Список уроков"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator | IsSuperuser]
    pagination_class = SchoolPagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Информация об уроке"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsMember | IsModerator | IsSuperuser]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Обновление урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator | IsSuperuser]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Удаление урока"""
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsSuperuser]


class SubscriptionViewSet(viewsets.ModelViewSet):
    """ViewSet для подписок"""

    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    lookup_field = 'id'

    def perform_create(self, serializer):
        """Сохранение подписки True или False для определенного пользователя"""
        new_subscription = serializer.save(user=self.request.user)
        new_subscription.save()
