from django import forms
from users.models import FacultyProfile

class FacultyProfileForm(forms.ModelForm):
    class Meta:
        model = FacultyProfile
        fields = ['employee_id', 'department']