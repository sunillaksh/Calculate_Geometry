"""Calculate_Geometry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('note_geometry.urls')), 
    path('', views.home, name='home'),
    path('Square/', views.Square),
    path('Rectangle/', views.Rectangle),
    path('Triangle/', views.Triangle),
    path('Circle/', views.Circle),
    path('Cube/', views.Cube),
    path('Cuboid/', views.Cuboid),
    path('Sphere/', views.Sphere),
    path('Cylinder/', views.Cylinder),
    path('Cone/', views.Cone),
]
