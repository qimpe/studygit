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


def is_in_favorite(func):
    def check(request, post_id):
        post = Post.objects.get(pk=post_id)
        favorite = FavoritePost.objects.filter(
            user_id=request.user.id, post_id=post_id
        ).exists()
        ic(favorite)
        data = {"favorite": favorite, "post_id": post_id}
        return func(request, data)

    return check


@is_in_favorite
def add_to_favorite(request, data):
    post_id = data["post_id"]
    post = get_object_or_404(Post, id=post_id)
    favorite_post = FavoritePost.objects.create(user=request.user, post=post)
    favorite_post.save()
    # return redirect("posts-detail", pk=post_id)
    return render(request, "posts-detail", pk=post_id, context={"favorite": True})


@is_in_favorite
def delete_from_favorite(request, data):
    post_id = data["post_id"]
    FavoritePost.objects.filter(user_id=request.user.id, post_id=post_id).delete()
    return redirect("posts-detail", pk=post_id)
