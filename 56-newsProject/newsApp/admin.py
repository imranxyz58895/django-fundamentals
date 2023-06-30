from . import models
from django.contrib import admin


@admin.register(models.Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'marks')
