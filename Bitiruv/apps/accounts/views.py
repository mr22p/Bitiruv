from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .models import Profile
from .forms import ProfileForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ro‘yxatdan o‘tdingiz! Endi login qiling.")
            return redirect("login")  # login url nomingiz boshqacha bo‘lsa o'zgartiring
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})

def home(request):
    # Hamma bitiruvchilar profillari
    profiles = Profile.objects.select_related('user').all()
    return render(request, 'home.html', {'profiles': profiles})


@login_required
def dashboard(request):
    # Login bo'lgan userning profili (bo'lsa)
    my_profile = Profile.objects.filter(user=request.user).first()

    # Hamma profillar (xohlasangiz exclude qilib qo'yamiz)
    profiles = Profile.objects.select_related('user').all()

    return render(request, 'dashboard.html', {
        'my_profile': my_profile,
        'profiles': profiles
    })


def profile_detail(request, username):
    user_obj = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user_obj)
    return render(request, 'profile_detail.html', {
        'profile': profile,
        'user_obj': user_obj
    })


@login_required
def create_profile(request):
    # Agar profil bor bo'lsa, qayta yaratmasin
    if Profile.objects.filter(user=request.user).exists():
        return redirect('profile_detail', username=request.user.username)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile_detail', username=request.user.username)
    else:
        form = ProfileForm()

    return render(request, 'create_profile.html', {'form': form})

@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})
