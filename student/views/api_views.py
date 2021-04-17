from rest_framework import views, viewsets, generics
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from student.models import (
    Student,
    ProgrammingLanguages
)
from student.serializers import (
    ProgrammingLanguagesSerializers,
    StudentSerializers
)


class StudentCreateAPIView(generics.ListCreateAPIView):
    serializer_class = StudentSerializers
    queryset = Student.objects.all()


class ProgrammingLanguagesCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProgrammingLanguagesSerializers
    queryset = ProgrammingLanguages.objects.all()
