from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import FavoritePost
from postsapp.models import Post
from icecream import ic
# Create your views here.


def bookmark(request):
    favorite_posts = FavoritePost.objects.all().filter(
        user_id=request.user.id
    )  # получаем список избранных постов у пользователя

    related_posts = [favorite.post for favorite in favorite_posts]
    # favorite - queryset
    # favorite.post отсылка класс Post
    ic(related_posts)
    return render(request, "bookmark.html", {"data": related_posts})


def add_to_favorite(request, post_id=0):
    post = get_object_or_404(Post, id=post_id)
    favorite_post = FavoritePost.objects.create(user=request.user, post=post)
    favorite_post.save()
    return redirect("posts-detail", pk=post_id)


def delete_from_favorite(request, post_id=0):
    favorite_posts = FavoritePost.objects.filter(
        user_id=request.user.id, post_id=post_id
    ).delete()
    return redirect("bookmark")


def is_in_favorite(request, post_id):
    post = Post.objects.get(pk=post_id)
    favorite = FavoritePost.objects.filter(
        user_id=request.user.id, post_id=post_id
    ).exists()
    data = {"favorite": favorite}
    return render(request, "posts-detail.html", data)
