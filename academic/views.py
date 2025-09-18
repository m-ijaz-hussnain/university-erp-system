from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CourseSchedule
from .forms import CourseScheduleForm

@login_required
def manage_schedules(request):
    if not request.user.is_superuser:
        return redirect('dashboard_redirect')
    schedules = CourseSchedule.objects.all()
    if request.method == 'POST':
        form = CourseScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_schedules')
    else:
        form = CourseScheduleForm()
    return render(request, 'academic/schedule_list.html', {'schedules': schedules, 'form': form})