from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from school.models import Course, Lesson
from school.permissions import IsOwner, IsModerator, IsMember, IsSuperuser
from school.serializers import CourseSerializer, LessonSerializer
from users.models import UserRoles


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.role != UserRoles.MODERATOR:
            return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if request.user.role != UserRoles.MODERATOR:
            return super().destroy(request, *args, **kwargs)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsMember | IsSuperuser]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator | IsSuperuser]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsMember | IsModerator | IsSuperuser]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator | IsSuperuser]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsSuperuser]
