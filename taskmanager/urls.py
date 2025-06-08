from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', lambda request: redirect('tasks:task_list'), name='root'),
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]