from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from school.models import Course, Lesson, Subscription
from school.permissions import IsOwner, IsModerator, IsMember, IsSuperuser
from school.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from users.models import UserRoles
from school.pagination import SchoolPagination


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с курсом"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = SchoolPagination

    def perform_create(self, request, *args, **kwargs):
        if request.user.role != UserRoles.MODERATOR:
            new_course = serializer.save()
            new_course.owner = self.request.user
            new_course.save()
            return super().create(request, *args, **kwargs)


    def destroy(self, request, *args, **kwargs):
        if request.user.role != UserRoles.MODERATOR:
            return super().destroy(request, *args, **kwargs)


class LessonCreateAPIView(generics.CreateAPIView):
    """Создание урока"""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsMember | IsSuperuser]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


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


