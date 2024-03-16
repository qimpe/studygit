from django.shortcuts import render


# Create your views here.
def homepagefunc(request):
    return render(request, "homepagetemplate.html")
