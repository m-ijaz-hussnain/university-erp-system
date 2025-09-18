from django import forms
from .models import FeeStructure, StudentFee

class FeeStructureForm(forms.ModelForm):
    class Meta:
        model = FeeStructure
        fields = ['program', 'year', 'amount']

class StudentFeeForm(forms.ModelForm):
    class Meta:
        model = StudentFee
        fields = ['student', 'fee_structure', 'amount_paid', 'due_date']