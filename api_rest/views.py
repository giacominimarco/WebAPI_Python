from django.shortcuts import redirect, render
# from django.http import HttpResponse, JsonResponse

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import UserSerializer
from .models import User

import json

def home(request):
    return render(request,'users/home.html')

def users(request):
    users = {
        'users': User.objects.all()
    }
    return render(request,'users/users.html',users)

def register(request):
    return render(request,'users/register.html')

def add(request):
    new_user = User()
    new_user.user_login = request.POST.get('login')
    new_user.user_password = request.POST.get('password')
    new_user.save()
    users = {
        'users': User.objects.all()
    }
    return render(request,'users/register.html')

def delete(request, login):
    user_delete = User.objects.get(pk=login)
    user_delete.delete()
    return render('users/users.html')
    # return render(request,'users/users.html',users)

# @api_view(['GET'])
# def get_users(request):
    
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#     return Response(status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT'])
# def get_by_login(request, login):
    
#     try:
#         user = User.objects.get(pk=login)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
#     return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','POST','PUT','DELETE'])
# def user_manager(request):
    
# # GET USER
#     if request.method == 'GET':
#         try:
#             user_login = request.GET['login']
            
#             try:
#                 user = User.objects.get(pk=user_login)
#             except:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
        
#             serializer = UserSerializer(user)
#             return Response(serializer.data)
        
#         except:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

# # SAVE USER
#     if request.method == 'POST':
#         new_user = request.data
#         serializer = UserSerializer(data=new_user)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
# # EDIT USER
#     if request.method == 'PUT':
#         login = request.data['user_login']
#         update_user = User.objects.get(pk=login)

#         try:
#             update_user = User.objects.get(pk=login)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         print(f'Data = {request.data}')
#         serializer = UserSerializer(update_user, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_CREATED)
        
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# # DELETE USER
#     if request.method == 'DELETE':
#         try:
#             user_delete = User.objects.get(pk=request.data['user_login'])
#             user_delete.delete()
#             return Response(status=status.HTTP_202_ACCEPTED)
#         except:
#             return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)