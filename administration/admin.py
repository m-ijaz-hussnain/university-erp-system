from django.contrib import admin
from .models import Department, Course, Batch

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'head']
    search_fields = ['name', 'code']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'credits', 'department']
    search_fields = ['code', 'name']

class BatchAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'department']
    search_fields = ['name']

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Batch, BatchAdmin)