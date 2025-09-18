from django.contrib import admin
from .models import StudentProfile, FacultyProfile

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'enrollment_number', 'batch', 'department']
    search_fields = ['user__username', 'enrollment_number']

class FacultyProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'employee_id', 'department']
    search_fields = ['user__username', 'employee_id']

admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(FacultyProfile, FacultyProfileAdmin)