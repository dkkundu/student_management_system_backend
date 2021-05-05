from rest_framework import serializers

from student.models import (
    Student,
    ProgrammingLanguages
)


class ProgramminglanguagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguages
        fields = ['name']


class StudentSerializers(serializers.ModelSerializer):
    programming_languages = ProgramminglanguagesSerializers(many=True)

    class Meta:
        model = Student
        fields = [
            'name',
            'age',
            'programming_languages',
        ]
