
from django.urls import path, include
from django.conf.urls import url

from student.views.api_views import (
    StudentCreateAPIView,
    ProgrammingLanguagesCreateAPIView,
)
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    url(r'^api/student/create/', StudentCreateAPIView.as_view()),
    url(r'^api/languages/create/', ProgrammingLanguagesCreateAPIView.as_view())
]
