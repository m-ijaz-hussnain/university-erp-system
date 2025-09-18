from django.urls import path
from . import views

urlpatterns = [
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('faculty/dashboard/', views.faculty_dashboard, name='faculty_dashboard'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('register/', views.register, name='register'),
]