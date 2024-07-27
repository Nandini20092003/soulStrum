"""
URL configuration for soulstrum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# soulstrum/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),  
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),  
    path('privacy/', TemplateView.as_view(template_name='privacy.html'), name='privacy'),  
    path('terms/', TemplateView.as_view(template_name='terms.html'), name='terms'),  
    path('', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  
    path('music/', include('music_catalog.urls')),
    path('playlists/', include('playlists.urls')),
    path('recommendations/', include('recommendations.urls')),
    path('social/', include('social_features.urls')),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
