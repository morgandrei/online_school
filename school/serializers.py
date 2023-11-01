from rest_framework import serializers
from school.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    les_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)

    def get_les_count(self, obj):
        return obj.lesson_set.all().count()

    class Meta:
        model = Course
        fields = ['__all__']
