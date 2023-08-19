from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .forms import CustomUserForm, CustomAuthenticationForm
from .models import CustomUser


# Create your views here.


class CustomRegisterView(CreateView):
    template_name = 'users/signin.html'
    form_class = CustomUserForm
    success_url = reverse_lazy('home')


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = CustomAuthenticationForm
    next_page = reverse_lazy('home')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class UserProfile(DetailView):
    model = CustomUser
    template_name = 'users/user_page.html'
