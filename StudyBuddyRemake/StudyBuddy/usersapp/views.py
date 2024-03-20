from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from .forms import LoginUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('create')

# Create your views here.
# def login_user(request):
#     if request.method == "POST":
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             error = "Данные введены неверно."
#             if user and user.is_active:
#                 login(request, user)
#                 error = ""
#                 return HttpResponseRedirect(reverse('homepage'))
#             else:
#                 error = "Неверные логин и пароль."
#     else:
#         form = LoginUserForm()
#         error = ""
#     data = {
#         'form':form,
#         'error':error
#     }
#     return render(request, 'login.html', data)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))

def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'createPost.html')
    else:
        form = RegisterUserForm
    return render(request, 'register.html', {'form': form})