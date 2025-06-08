from django.urls import path, include  # Added include
from django.views.generic import TemplateView  # Added missing import
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from . import views
from django.contrib.auth.views import LogoutView  # Nouveau style (Django 3.1+)
from django.contrib.auth.views import LogoutView
from django.views.decorators.http import require_POST
app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('update/<int:pk>/', views.update_task, name='update_task'),
    
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('toggle/<int:pk>/', csrf_exempt(views.toggle_complete), name='toggle_complete'),
     path('accounts/logout/', 
         require_POST(LogoutView.as_view(template_name='registration/logged_out.html')), 
         name='logout'),
    # Only keep one accounts home view (removed duplicate)
    path('accounts/', login_required(TemplateView.as_view(template_name='accounts/home.html')), name='accounts_home'),
    
    # Auth URLs - moved to project's main urls.py (recommended)
    # path('accounts/', include('django.contrib.auth.urls')),
]