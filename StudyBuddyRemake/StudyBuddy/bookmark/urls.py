from django.contrib import admin
from django.urls import path, include
from .views import bookmark, add_to_favorite

urlpatterns = [
    path("", bookmark, name="bookmark"),
    path("add-to-favorite/<int:post_id>/", add_to_favorite, name="add_to_favorite"),
]
