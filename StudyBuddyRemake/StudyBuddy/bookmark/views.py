from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import FavoritePost
from postsapp.models import Post
from icecream import ic
# Create your views here.


def bookmark(request):
    """favorite_posts = FavoritePost.objects.filter(user_id=request.user.id).values(
        "user_id", "post_id"
    )
    # ic(favorite_posts)
    for i in favorite_posts:
        # posts = Post.objects.get(pk=int("post_id"))
        posts = Post.objects.get(id="post_id")
    ic(posts)

    print("post id is == ", "post_id")
    favorite_posts_dict = {}
    post_ids = []
    for post in favorite_posts.values():
        post_id = post["post_id"]
        posts = Post.objects.get(pk=post_id)
        print(posts)
    favorite_posts_dict["posts"] = post_ids
    print(favorite_posts_dict)
    for post in favorite_posts_dict.items():
        print(post[1])
    return render(request, "bookmark.html", {"posts": posts})"""

    # return render(request, "bookmark.html", favorite_posts_dict)
    """favorite_posts = FavoritePost.objects.all().filter(user_id=request.user.id)
    post_ids = favorite_posts.values_list("post_id", flat=True)
    posts = Post.objects.all().filter(id__in=post_ids)
    print(posts)"""

    favorite_posts = FavoritePost.objects.filter(user_id=request.user.id).values(
        "user_id", "post_id"
    )
    ids = []
    for i in favorite_posts:
        ids.append(i["post_id"])
    ic(ids)
    for i in ids:
        posts = Post.objects.get(pk=i)
    data = {"posts": posts}
    return redirect(request, "bookmark.html", data)


def add_to_favorite(request, post_id=0):
    post = get_object_or_404(Post, id=post_id)
    favorite_post = FavoritePost.objects.create(user=request.user, post=post)
    favorite_post.save()
    return redirect("posts-detail", pk=post_id)


def delete_from_favorite(request, post_id=0):
    favorite_posts = FavoritePost.objects.filter(
        user_id=request.user.id, post_id=post_id
    ).delete()


"""def is_in_favorite(post_id):
    is_exists = FavoritePost.objects.filter(post_id=post_id).exists()
    ic(is_exists)"""
