from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

app_name = "users"

urlpatterns = [
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register, name="register")
]
