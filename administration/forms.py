from django import forms
from .models import Department, Course, Batch

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'code', 'head']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name', 'credits', 'department', 'taught_by']

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['name', 'year', 'department', 'students']