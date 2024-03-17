from django.contrib import admin
from django.urls import path, include
from .views import bookmark

urlpatterns = [
    path("", bookmark, name="bookmark"),
]
