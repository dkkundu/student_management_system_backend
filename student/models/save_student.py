# DJANGO IMPORTE

from django.db import models
from django.utils.translation import gettext_lazy as _


class ProgrammingLanguages(models.Model):
    name = models.CharField(
        _("Programming Name"), max_length=50, blank=False,
        null=False
    )
    code = models.PositiveIntegerField(
        _("Code"), null=True, blank=True
    )

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(
        _("Student Name"), max_length=50, null=False,
        blank=False
    )
    age = models.PositiveIntegerField(
        _("Age"), null=False, blank=False
    )
    programming_languages = models.CharField(
        _("Programming Languages"), max_length=50,
        null=True

    )

    def __str__(self):
        return f'name: {self.name}, Age: {str(self.age)}'
