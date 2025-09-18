from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    head = models.ForeignKey('users.FacultyProfile', on_delete=models.SET_NULL, null=True, blank = True, related_name='headed_department')

    def __str__(self):
        return self.name

class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    credits = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    taught_by = models.ManyToManyField('users.FacultyProfile')

    def __str__(self):
        return self.code

class Batch(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    students = models.ManyToManyField('users.StudentProfile', related_name='batches')

    def __str__(self):
        return f"{self.name} - {self.year}"