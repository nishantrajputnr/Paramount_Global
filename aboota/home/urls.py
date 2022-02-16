from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checking),
    path('about-us/',views.about, name='about'),
    path('product/',views.product,name="product")
]

