from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Department, Course, Batch
from .forms import DepartmentForm, CourseForm, BatchForm

@login_required
def manage_departments(request):
    if not request.user.is_superuser:
        return redirect('dashboard_redirect')
    departments = Department.objects.all()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_departments')
    else:
        form = DepartmentForm()
    return render(request, 'administration/department_list.html', {'departments': departments, 'form': form})

@login_required
def manage_courses(request):
    if not request.user.is_superuser:
        return redirect('dashboard_redirect')
    courses = Course.objects.all()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_courses')
    else:
        form = CourseForm()
    return render(request, 'administration/course_list.html', {'courses': courses, 'form': form})

@login_required
def manage_batches(request):
    if not request.user.is_superuser:
        return redirect('dashboard_redirect')
    batches = Batch.objects.all()
    if request.method == 'POST':
        form = BatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_batches')
    else:
        form = BatchForm()
    return render(request, 'administration/batch_list.html', {'batches': batches, 'form': form})