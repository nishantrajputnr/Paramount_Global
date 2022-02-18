from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checking),
    path('about-us/',views.about, name='about'),
    path('product/',views.product,name="product"),
    path('education/',views.education,name="education"),
    path('trading/',views.trading,name="trading"),
    path('terminal/',views.terminal,name="terminal"),
    path('referal/',views.referal,name="referal"),
]


