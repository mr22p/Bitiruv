from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from apps.accounts import views  # sizning home view joylashgan app

urlpatterns = [
    path('admin/', admin.site.urls),

    # HOME
    path('', views.home, name='home'),

    # LOGIN
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),

    # LOGOUT
    path('logout/', auth_views.LogoutView.as_view(
        next_page='home'
    ), name='logout'),
]
