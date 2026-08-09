from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
    path('',home, name="home"),
    path('gallery/',gallery, name="gallery"),
    path('bgremove/',bgremove, name="bgremove"),
    path('contact/',contact, name="contact"),
    path('about/',about, name="about"),
]
