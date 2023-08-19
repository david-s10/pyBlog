from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms import forms

from .models import CustomUser


class CustomAuthenticationForm(AuthenticationForm):
    pass


class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'avatar')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('avatar', 'about')

