from django.contrib import admin
from django.urls import path, include
from users import views as users_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('administration/', include('administration.urls')),
    path('student/', include('student.urls')),
    path('faculty/', include('faculty.urls')),
    path('academic/', include('academic.urls')),
    path('library/', include('library.urls')),
    path('accounting/', include('accounting.urls')),
    path('reporting/', include('reporting.urls')),
    path('dashboard/', include('users.urls')),
    path('', users_views.dashboard_redirect, name='home'),
    # path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]