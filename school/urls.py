from django.urls import path
from rest_framework.routers import DefaultRouter
from school.apps import SchoolConfig
from school.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView

app_name = SchoolConfig.name

router = DefaultRouter()
router.register(r'school', CourseViewSet, basename='school')
urlpatterns = [
    path('lesson/create', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name= 'lesson-list'),

] + router.urls
