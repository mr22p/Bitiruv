from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/create/', views.create_profile, name='create_profile'),
    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),
]