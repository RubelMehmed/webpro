from django.contrib import admin
from .models import Teacher, Course, Department

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Department)