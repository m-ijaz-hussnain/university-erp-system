from django.db import models

class Attendance(models.Model):
    student = models.ForeignKey('users.StudentProfile', on_delete=models.CASCADE)
    course = models.ForeignKey('administration.Course', on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])

class Grade(models.Model):
    student = models.ForeignKey('users.StudentProfile', on_delete=models.CASCADE)
    course = models.ForeignKey('administration.Course', on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)

class CourseSchedule(models.Model):
    course = models.ForeignKey('administration.Course', on_delete=models.CASCADE)
    faculty = models.ForeignKey('users.FacultyProfile', on_delete=models.CASCADE)
    semester = models.CharField(max_length=20)
    timings = models.CharField(max_length=50)
    classroom = models.CharField(max_length=50)