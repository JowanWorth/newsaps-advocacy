from django.contrib import admin
from django.urls import path, include
from main import views  # Import views from your main app

urlpatterns = [
    path('', views.home, name='home'),  # Directly reference the home view
    path('accounts/', include('accounts.urls')),
    path('forum/', include('forum.urls')),
    # Add other specific paths from your main app here
]
