from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('login/' , employee_login, name="login"),
    path('logout/' , employee_logout, name="logout"),
]