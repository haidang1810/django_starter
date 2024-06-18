from django.contrib import admin
from django.urls import path
from . import views as cms

urlpatterns = [
    path('', cms.index),
]
