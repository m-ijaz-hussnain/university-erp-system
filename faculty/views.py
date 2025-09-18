from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import FacultyProfile
from academic.models import Attendance, Grade, CourseSchedule
from .forms import FacultyProfileForm
from academic.forms import AttendanceForm, GradeForm

@login_required
def faculty_profile(request):
    profile = request.user.faculty_profile
    if request.method == 'POST':
        form = FacultyProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('faculty_dashboard')
    else:
        form = FacultyProfileForm(instance=profile)
    return render(request, 'faculty/profile.html', {'form': form})

@login_required
def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty_dashboard')
    else:
        form = AttendanceForm()
    return render(request, 'faculty/mark_attendance.html', {'form': form})

@login_required
def assign_grades(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty_dashboard')
    else:
        form = GradeForm()
    return render(request, 'faculty/assign_grades.html', {'form': form})