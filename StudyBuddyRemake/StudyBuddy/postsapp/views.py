from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Post, FavoritePost


# Create your views here.
def mainpage(request):
    search_query = request.GET.get("postsSearchArea", None)
    search_query_filter = request.GET.get("filter", None)
    if search_query:
        for i in search_query.split():
            posts = Post.objects.filter(
                Q(title__iregex=i)
                | Q(about__iregex=i)
                | Q(goalperson__iregex=i)
                | Q(tags__iregex=i)
                | Q(additional__iregex=i)
            )
    else:
        if search_query_filter:
            posts = Post.objects.filter(tags__iregex=search_query_filter)
        else:
            posts = Post.objects.all()
    if posts:
        infoText = ""
    else:
        posts = None
        infoText = "Анкеты не найдены. Воспользуйтесь фильтрами или обновите поиск."
    data = {"posts": posts, "infoText": infoText}
    return render(request, "postsapp/postspage.html", data)


class postsDetailView(DetailView):
    model = Post
    template_name = "postsapp/postsDetailViewTemplate.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = context["post"].title
        context['is_favorite'] = FavoritePost.objects.filter(user=self.request.user, post=self.get_object()).exists()
        return context

def bookmarks(request):
    related_posts = FavoritePost.objects.filter(user=request.user)
    posts = [favorite.post for favorite in related_posts]
    return render(request, 'postsapp/bookmark.html', {'posts': posts})

def create(request):
    return render(request, "postsapp/createPost.html")


def add_to_favorites(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if FavoritePost.objects.filter(user=request.user, post=post).exists():
        pass
    else:
        FavoritePost.objects.create(user=request.user, post=post)
    return redirect('posts-detail', pk=post_id)

def del_from_favorites(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if FavoritePost.objects.filter(user=request.user, post=post).exists():
        FavoritePost.objects.filter(user=request.user, post=post).delete()
    return redirect('posts-detail', pk=post_id)