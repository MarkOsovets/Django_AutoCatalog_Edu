from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginUserForm, ProfileUserForm, RegisterUserForm, UserPasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your views here.
# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUser(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd["username"], password=cd["password"])
#             if user and user.is_active:
#                 login(request, user)
#                 return redirect('index')
#     else:    
#         form = LoginUser()
#     return render(request, 'users/login.html', {'form':form})    

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('index')

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
            return render(request, 'users/register_done.html', {'new_user': user})
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('users:login')


class ProfileUser(CreateView, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {
        'title': "Профиль пользователя",
        'default_image': settings.DEFAULT_USER_IMAGE,
        }

    def get_success_url(self):
        return reverse_lazy('users:profile')
    
    def get_object(self, queryset=None):
        return self.request.user
    

class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"
