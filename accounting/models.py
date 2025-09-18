from django.db import models

class FeeStructure(models.Model):
    program = models.CharField(max_length=100)
    year = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class StudentFee(models.Model):
    student = models.ForeignKey('users.StudentProfile', on_delete=models.CASCADE)
    fee_structure = models.ForeignKey(FeeStructure, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()