from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import StudentProfile, FacultyProfile
from academic.models import Attendance, Grade
from accounting.models import StudentFee

@login_required
def student_report(request):
    students = StudentProfile.objects.all()
    return render(request, 'reporting/student_report.html', {'students': students})

@login_required
def faculty_report(request):
    faculty = FacultyProfile.objects.all()
    return render(request, 'reporting/faculty_report.html', {'faculty': faculty})

@login_required
def academic_report(request):
    grades = Grade.objects.all()
    return render(request, 'reporting/academic_report.html', {'grades': grades})

@login_required
def financial_report(request):
    fees = StudentFee.objects.all()
    return render(request, 'reporting/financial_report.html', {'fees': fees})