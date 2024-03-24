from django.contrib import admin
from django.urls import path, include
from .views import bookmark, add_to_favorite, delete_from_favorite

urlpatterns = [
    path("", bookmark, name="bookmark"),
    path(
        "add-to-favorite/<int:post_id>/",
        add_to_favorite,
        name="add_to_favorite",
    ),
    path(
        "delete_from_favorite/<int:post_id>/",
        delete_from_favorite,
        name="delete_from_favorite",
    ),
]
