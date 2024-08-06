from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('users/', views.users, name='users'),
    path('register/', views.register, name='register'),
    path('add/', views.add, name='add'),
    path('users/delete/<str:username>', views.delete, name='delete'),
]
