from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checking),
    path('template3d/',views.template3d, name='about'),
    path('template/',views.template)
]


