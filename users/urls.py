from django.urls import path
from django.contrib.auth import views as auth_views

from users.views import create_user

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', create_user, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]