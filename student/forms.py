from django import forms
from users.models import StudentProfile

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['enrollment_number', 'batch', 'department']