from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'project_name', 'project_description', 'project_link']

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Foydalanuvchi nomi",
        help_text="150 ta belgigacha. Harflar va raqamlar."
    )

    password1 = forms.CharField(
        label="Parol",
        widget=forms.PasswordInput,
        help_text="Parol kamida 8 ta belgidan iborat bo'lishi kerak."
    )

    password2 = forms.CharField(
        label="Parolni tasdiqlang",
        widget=forms.PasswordInput,
        help_text="Xavfsizlik uchun parolni qayta kiriting."
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

     