import logging
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, login, logout
from django.contrib import messages
from .forms import RegistrationForm
from academic.models import Grade, Attendance
from accounting.models import StudentFee
from library.models import Borrowing
from administration.models import Course,Department

logger = logging.getLogger(__name__)

User = get_user_model()

def dashboard_redirect(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')  # Show homepage for unauthenticated users
    user = request.user
    if user.is_superuser:
        return redirect('admin_dashboard')
    elif hasattr(user, 'student_profile'):
        return redirect('student_dashboard')
    elif hasattr(user, 'faculty_profile'):
        return redirect('faculty_dashboard')
    else:
        logout(request)  # Log out users with no recognized profile
        return render(request, 'index.html')  # Return to homepage after logout

@login_required
def student_dashboard(request):
    profile = request.user.student_profile
    context = {'profile': profile}
    
    try:
        # Fetch related data
        grades = Grade.objects.filter(student=profile)
        attendance = Attendance.objects.filter(student=profile)
        courses = Course.objects.filter(grade__student=profile).distinct()  # Via Grade
        student_fees = StudentFee.objects.filter(student=profile)
        borrowed_books = Borrowing.objects.filter(user=profile.user)
        logger.info(f'Student {profile.user.username} - All Borrowings: {[b.book_copy.book.title for b in borrowed_books if b.book_copy and b.book_copy.book]}')
        active_borrowed_books = Borrowing.objects.filter(user=profile.user, return_date__isnull=True)
        department = profile.department

        # Log detailed data for debugging
        logger.info(f"Student {profile.user.username} - Grades: {grades.count()} {[g.grade for g in grades]}, "
                    f"Courses: {courses.count()} {[c.name for c in courses]}, "
                    f"Fees: {student_fees.count()} {[f.amount_paid for f in student_fees]}, "
                    f"Active Borrowed Books: {active_borrowed_books.count()} {[b.book_copy.book.title for b in active_borrowed_books if b.book_copy and b.book_copy.book]}")

        context.update({
            'grades': grades,
            'attendance': attendance,
            'courses': courses,
            'student_fees': student_fees,
            'borrowed_books': active_borrowed_books,
            'department': department,
        })
    except Exception as e:
        logger.error(f"Error in student_dashboard for {profile.user.username}: {str(e)}")
        context['error'] = f"Error loading data: {str(e)}"

    return render(request, 'users/student_dashboard.html', context)

@login_required
def faculty_dashboard(request):
    profile = request.user.faculty_profile
    return render(request, 'users/faculty_dashboard.html', {'profile': profile})

@login_required
def admin_dashboard(request):
    return render(request, 'users/admin_dashboard.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})