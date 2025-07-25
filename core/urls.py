"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from accounts.views import PasswordResetRequestAPIView, PasswordResetConfirmAPIView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),  # Admin-Panel
    path('api/accounts/', include('accounts.urls')),  # Accounts-URLs
    path('api/videos/', include('videos.urls')),  # Videos-URLs
    path('django-rq/', include('django_rq.urls')),  # RQ-Monitoring

    path('password-reset-request/', PasswordResetRequestAPIView.as_view(), name='password-reset-request'),
    path('reset-password/confirm/', PasswordResetConfirmAPIView.as_view(), name='password-reset-confirm'),

]

if settings.DEBUG:
    # Media-Dateien unter /videoflix/media/ bereitstellen
    urlpatterns += static('/videoflix/media/', document_root=settings.MEDIA_ROOT)