from django.urls import path
from . import views

urlpatterns = [
    path('schedules/', views.manage_schedules, name='manage_schedules'),
]