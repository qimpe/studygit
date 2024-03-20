from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Post


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
        return context


def create(request):
    return render(request, "postsapp/createPost.html")
