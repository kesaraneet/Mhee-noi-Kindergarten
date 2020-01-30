from django.contrib import admin
from django.urls import path
from check import views

urlpatterns = [
    path('', views.index),
    path('course/<int:id>', views.course),
    path('qrcode', views.qrcode)
]