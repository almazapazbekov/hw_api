"""api URL Configuration

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
# from rest_framework.routers import DefaultRouter
# from employees import views


from employees.views import get_position, get_employees, new_position\
    , new_employees

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_position/', get_position, name='get_position'),
    path('get_employees/', get_employees, name='get_employees'),
    path('new_position/', new_position, name='new_position'),
    path('new_employees/', new_employees, name='new_employees'),

]
