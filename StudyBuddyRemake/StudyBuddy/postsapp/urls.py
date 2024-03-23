from django.urls import path, include
from . import views
from .views import add_to_favorites, del_from_favorites, bookmarks

urlpatterns = [
    path("", views.mainpage, name="postslink"),
    path("<int:pk>", views.postsDetailView.as_view(), name="posts-detail"),
    path('create/', views.create, name="create"),
    path('post/<int:post_id>/add_to_favorites/', add_to_favorites, name='add_to_favorites'),
    path('post/<int:post_id>/del_from_favorites/', del_from_favorites, name='del_from_favorites'),
    path('bookmarks', bookmarks, name='bookmarks')
]
