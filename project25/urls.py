"""project25 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from os import name
from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fun_register/',fun_register,name='fun_register'),
    path('fun_home/',fun_home,name='fun_home'),
    path('fun_login/',fun_login,name='fun_login'),
    path('fun_logout/',fun_logout,name='fun_logout'),
    path('fun_profile/',fun_profile,name='fun_profile'),
    path('fun_changepassword/',fun_changepassword,name='fun_changepassword'),
    path('fun_forgotpassword/',fun_forgotpassword,name='fun_forgotpassword'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
