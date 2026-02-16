from django.shortcuts import render
from accounts.models import Profile

def home(request):
    profiles = Profile.objects.all()
    return render(request, 'home.html', {'profiles': profiles})
