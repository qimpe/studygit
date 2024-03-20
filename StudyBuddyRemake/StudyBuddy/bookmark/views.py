from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import FavoritePost
from postsapp.models import Post
# Create your views here.


def bookmark(request):
    favorite_posts = (
        FavoritePost.objects.all()
        .filter(user_id=request.user.id)
        .values("user_id", "post_id")
    )
    favorite_posts_dict = {}
    post_ids = []
    for post in favorite_posts.values():
        post_ids.append(post["post_id"])
        posts = Post.objects.get(pk=post_id)

    favorite_posts_dict["posts"] = post_ids
    print(favorite_posts_dict)
    for post in favorite_posts_dict.items():
        print(post[1])

    

    
    return render(request, "bookmark.html", favorite_posts_dict)
    """favorite_posts = FavoritePost.objects.all().filter(user_id=request.user.id)
    post_ids = favorite_posts.values_list("post_id", flat=True)
    posts = Post.objects.all().filter(id__in=post_ids)
    print(posts)"""


def add_to_favorite(request, post_id=0):
    post = get_object_or_404(Post, id=post_id)
    favorite_post = FavoritePost.objects.create(user=request.user, post=post)
    favorite_post.save()
    return redirect("posts-detail", pk=post_id)


def delete_from_favorite(request, post_id=0): ...
