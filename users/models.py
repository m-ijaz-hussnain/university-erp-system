from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    enrollment_number = models.CharField(max_length=20, unique=True)
    batch = models.ForeignKey('administration.Batch', on_delete=models.SET_NULL, null=True, blank = True, related_name = 'student_profile')
    department = models.ForeignKey('administration.Department', on_delete=models.SET_NULL, null=True, blank = True, related_name = 'student_profile')

    def __str__(self):
        return f"{self.user.username} - Student"

class FacultyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='faculty_profile')
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey('administration.Department', on_delete=models.SET_NULL, null=True, blank = True, related_name = 'faculty_profile')

    def __str__(self):
        return f"{self.user.username} - Faculty"