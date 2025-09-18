from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FeeStructure, StudentFee
from .forms import FeeStructureForm, StudentFeeForm

@login_required
def manage_fees(request):
    if not request.user.is_superuser:
        return redirect('dashboard_redirect')
    fees = FeeStructure.objects.all()
    if request.method == 'POST':
        form = FeeStructureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_fees')
    else:
        form = FeeStructureForm()
    return render(request, 'accounting/fee_list.html', {'fees': fees, 'form': form})

@login_required
def student_fees(request):
    profile = request.user.student_profile
    fees = StudentFee.objects.filter(student=profile)
    return render(request, 'accounting/student_fees.html', {'fees': fees})