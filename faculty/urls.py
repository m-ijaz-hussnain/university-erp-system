from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.faculty_profile, name='faculty_profile'),
    path('attendance/mark/', views.mark_attendance, name='mark_attendance'),
    path('grades/assign/', views.assign_grades, name='assign_grades'),
]