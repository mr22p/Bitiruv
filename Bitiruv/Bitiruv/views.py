from accounts.models import Profile
from django.shortcuts import render

def home(request):
    profiles = Profile.objects.all()
    return render(request, 'home.html', {'profiles': profiles})
