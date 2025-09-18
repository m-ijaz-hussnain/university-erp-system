from django.urls import path
from . import views

urlpatterns = [
    path('fees/', views.manage_fees, name='manage_fees'),
    path('student/fees/', views.student_fees, name='student_fees'),
]