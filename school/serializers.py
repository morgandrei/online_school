from rest_framework import serializers
from school.models import Course, Lesson, Subscription
from school.validators import LessonUrlValidator
from users.serializers import UserSerializer


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [
            LessonUrlValidator(field='url'),
            serializers.UniqueTogetherValidator(fields=['title', 'url'], queryset=Lesson.objects.all())
        ]


class CourseSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    les_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)
    subscribers = SubscriptionSerializer(many=True, read_only=True)

    def get_les_count(self, obj):
        return obj.lesson_set.all().count()

    class Meta:
        model = Course
        fields = '__all__'
