from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.academy.apps import AcademyConfig
from apps.academy.views import LessonModelViewSet
from apps.academy import views


router = DefaultRouter()
router.register(r'api/lesson', LessonModelViewSet, basename='lessons')

app_name = AcademyConfig.name

urlpatterns = [
    path('api/course/create/', views.CourseCreateAPIView.as_view(), name='course_create'),
    path('api/course/', views.CourseListAPIView.as_view(), name='course_list'),
    path('api/course/<int:pk>/', views.CourseRetrieveAPIView.as_view(), name='course_retrieve'),
    path('api/course/update/<int:pk>/', views.CourseUpdateAPIView.as_view(), name='course_update'),
    path('api/course/delete/<int:pk>/', views.CourseDestroyAPIView.as_view(), name='course_destroy'),

    path('api/subscription/', views.CreateSubscriptionAPIView.as_view(), name='subscription_create'),
    path('api/subscription/delete/<int:pk>/', views.DestroySubscriptionAPIView.as_view(), name='subscription_create'),
]

urlpatterns += router.urls