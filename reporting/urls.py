from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student_report, name='student_report'),
    path('faculty/', views.faculty_report, name='faculty_report'),
    path('academic/', views.academic_report, name='academic_report'),
    path('financial/', views.financial_report, name='financial_report'),
]