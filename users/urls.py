"""Определяет схемы URL для пользователей"""
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout

from . import views

urlpatterns = [
    # Страница входа
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # Страница выхода
    path('logout/', views.logout_view, name='logout'),
    # Страница регистрации
    path('register/', views.register, name='register'),
]
