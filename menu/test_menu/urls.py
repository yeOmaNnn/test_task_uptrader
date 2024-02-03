from django.contrib import admin
from django.urls import path, re_path
from .views import show_menu

urlpatterns = [
    path('', show_menu, name='show_menu'),
    re_path(r'^[a-zA-Z0-9]+$', show_menu, name='show_menu'),
]
