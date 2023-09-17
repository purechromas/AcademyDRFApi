from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.academy.models import Course, Lesson
from apps.academy.serializers import CourseSerializer, LessonSerializer
from config.perms import ModeratorNotAllow, ModeratorAllow, IsObjectOwner, ModeratorAndObjectCreatorAllow


class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, ModeratorNotAllow]

class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.groups.filter(name='Moderators').exists():
            return Course.objects.all()
        return Course.objects.filter(creator=self.request.user)

class CourseRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsObjectOwner]

class CourseUpdateAPIView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, ModeratorAllow | IsObjectOwner]

class CourseDestroyAPIView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsObjectOwner]

class LessonModelViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ModeratorAndObjectCreatorAllow]




