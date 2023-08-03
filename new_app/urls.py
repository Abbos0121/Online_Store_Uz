from django.contrib import admin
from django.urls import path, include
from .views import profile_view
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile_view'),
]
