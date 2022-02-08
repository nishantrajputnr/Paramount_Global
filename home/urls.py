from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.fun1),
    path('hello/',views.hello)
]


