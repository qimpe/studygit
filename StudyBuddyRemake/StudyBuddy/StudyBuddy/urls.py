from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("homepage.urls")),
    path("posts/", include("postsapp.urls")),
    path("users/", include("usersapp.urls", namespace="users")),
    path("bookmark/", include("bookmark.urls")),
]
