from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.student_profile, name='student_profile'),
    path('attendance/', views.view_attendance, name='view_attendance'),
    path('grades/', views.view_grades, name='view_grades'),
]