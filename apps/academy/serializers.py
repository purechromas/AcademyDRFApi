from rest_framework import serializers

from apps.academy.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Lesson
        fields = ('id', 'name', 'preview', 'description', 'course', 'creator')


class CourseSerializer(serializers.ModelSerializer):
    lessons_quantity = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(read_only=True, many=True)
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    @staticmethod
    def get_lessons_quantity(course):
        return course.lessons.all().count()

    class Meta:
        model = Course
        fields = ('id', 'name', 'preview', 'description', 'lessons', 'lessons_quantity', 'creator')

