# DJANGO IMPORTS
from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import (
    ProgrammingLanguages,
    Student
)


class ProgrammingLanguagesResources(resources.ModelResource):

    class Meta:
        model = ProgrammingLanguages


@admin.register(ProgrammingLanguages)
class ProgrammingLanguagesAdmin(ImportExportModelAdmin):
    model = ProgrammingLanguages

    list_display = [
        'name', 'code'
    ]

    search_fields = [
        'name',
    ]

    ordering = [
        'name'
    ]
    resource_class = ProgrammingLanguagesResources


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    model = Student

    list_display = [
        'name', 'age'
    ]

    search_fields = ['name']

    ordering = ['name']

    resource_class = StudentResource
