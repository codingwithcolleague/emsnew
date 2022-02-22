from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('' , index, name="list"),
    path('<int:id>/details/' , details, name="details"),
    path('<int:id>/' , poll, name="poll"),
    path('<int:id>/poll/' , polldetails, name="polldetails"),


]
