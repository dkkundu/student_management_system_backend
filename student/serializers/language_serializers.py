from student.models import ProgrammingLanguages
from rest_framework import serializers


class ProgrammingLanguagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguages
        fields = [
            "name",
            'code',
        ]
