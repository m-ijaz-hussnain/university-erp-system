from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.manage_departments, name='manage_departments'),
    path('courses/', views.manage_courses, name='manage_courses'),
    path('batches/', views.manage_batches, name='manage_batches'),
]