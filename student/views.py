from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import StudentProfile
from academic.models import Attendance, Grade
from .forms import StudentProfileForm

@login_required
def student_profile(request):
    profile = request.user.student_profile
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('student_dashboard')
    else:
        form = StudentProfileForm(instance=profile)
    return render(request, 'student/profile.html', {'form': form})

@login_required
def view_attendance(request):
    profile = request.user.student_profile
    attendance = Attendance.objects.filter(student=profile)
    return render(request, 'student/attendance.html', {'attendance': attendance})

@login_required
def view_grades(request):
    profile = request.user.student_profile
    grades = Grade.objects.filter(student=profile)
    return render(request, 'student/grades.html', {'grades': grades})