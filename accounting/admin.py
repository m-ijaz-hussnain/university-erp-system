from django.contrib import admin
from .models import FeeStructure, StudentFee

class FeeStructureAdmin(admin.ModelAdmin):
    list_display = ['program', 'year', 'amount']
    search_fields = ['program']

class StudentFeeAdmin(admin.ModelAdmin):
    list_display = ['student', 'fee_structure', 'amount_paid', 'due_date']
    search_fields = ['student__user__username']

admin.site.register(FeeStructure, FeeStructureAdmin)
admin.site.register(StudentFee, StudentFeeAdmin)