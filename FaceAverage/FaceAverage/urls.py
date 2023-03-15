"""FaceAverage URL Configuration

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
from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.main, name='main'),
    path('face_average/<str:gender>/<int:id>', mainapp.face_average, name='face_average'),
    path('face_average/<str:gender>', mainapp.face_average_gender, name='face_average_gender'),
    path('like/<str:gender>/<int:id>', mainapp.like, name='like'),
    path('delete/', mainapp.delete, name='delete'),
    path('create_img/<str:gender>/<str:ids>', mainapp.create_img, name='create_img'),
]
