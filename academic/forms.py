from django import forms
from .models import Grade, CourseSchedule, Attendance

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'course', 'grade']

class CourseScheduleForm(forms.ModelForm):
    class Meta:
        model = CourseSchedule
        fields = ['course', 'faculty', 'semester', 'timings', 'classroom']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'course', 'date', 'status']