from django.contrib import admin
from .models import Attendance, Grade, CourseSchedule

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'date', 'status']
    search_fields = ['student__user__username', 'course__code']

class GradeAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'grade']
    search_fields = ['student__user__username', 'course__code']

class CourseScheduleAdmin(admin.ModelAdmin):
    list_display = ['course', 'faculty', 'semester', 'timings']
    search_fields = ['course__code', 'faculty__user__username']

admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(CourseSchedule, CourseScheduleAdmin)