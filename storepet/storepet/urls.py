"""storepet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from storepet.views import index
from storepet.views import galeria
from storepet.views import servicio
from storepet.views import registro
from storepet.views import contacto



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index/', index),
    path('galeria/', galeria),
    path('servicio/', servicio),
    path('registro/', registro),
    path('contacto/',contacto),

    

    
]
