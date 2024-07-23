from django.contrib import admin
from teacher.models import Teacher_2
# Register your models here.
@admin.register(Teacher_2)
class teacherss(admin.ModelAdmin):
    list_display = ['id','F_name']