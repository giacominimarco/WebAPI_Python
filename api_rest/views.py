from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as login_django, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as User_Django

def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        login = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(username=login, password=password)
        if user is not None:
            login_django(request, user)
            return render(request,'users/home.html')
        else:
            return HttpResponse('Login or password invalid')
        
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url="/auth/login/")
def home(request):
    return render(request,'users/home.html')


@login_required(login_url="/auth/login/")
def users(request):
    users = {
        'users': User_Django.objects.all()
    }
    return render(request,'users/users.html',users)


def register(request):
    return render(request,'users/register.html')


def add(request):
    new_login = request.POST.get('login')
    new_password = request.POST.get('password')
    hasUser = User_Django.objects.filter(username=new_login).first()
    if hasUser:
        return render(request,'users/register.html')
    new_user = User_Django.objects.create_user(username=new_login, password=new_password)
    new_user.save()
    return render(request,'users/register.html')


@login_required(login_url="/auth/login/")
def delete(request, username):
    user_delete = User_Django.objects.get(username=username)
    user_delete.delete()
    users = {
        'users': User_Django.objects.all()
    }
    return render(request,'users/users.html',users)