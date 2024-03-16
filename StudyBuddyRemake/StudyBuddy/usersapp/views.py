from django.shortcuts import render


# Create your views here.
def login_user(request):
    return render(request, 'layout.html')

def logout_user(request):
    return render(request, 'layout.html')