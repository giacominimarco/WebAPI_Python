from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.users, name='users'),
    path('register/', views.register, name='register'),
    path('add/', views.add, name='add'),
    path('delete/<str:login>/', views.delete, name='delete'),

    # path('', views.get_users, name='get_all_users'),
    # path('user/<str:login>', views.get_by_login, name='get_by_login'),
    # path('data/', views.user_manager, name='user_manager'),
]
