from os import stat
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
import json

class Signup(APIView):
  def post(self, request):
    data = json.loads(request.body.decode('utf-8'))
    
    user = User.objects.create_user(
      email = data["email"],
      name = data["name"],
      nickname = data["nickname"],
      birth = data["birth"],
      phonenumber = data["phone"],
      password = data["password"]
    )
    token = Token.objects.create(user=user)
    return Response({"Token": token.key})

class Login(APIView):
  def post(self, request):
    data = json.loads(request.body)
    user = auth.authenticate(username=data["email"], password=data["password"])
    if (user is not None):
      token = Token.objects.get(user=user)
      if (token is None):
        token = Token.objects.create(user=user)
      return Response({"Token": token})
    else:
      return Response(status=401)

class Logout(APIView):
  def get(self, request):
    user = request.user
    Token.objects.delete(user=user)
    return Response({"Logout"})

class ChangePassword(APIView):
  def post(self, request):
    data = json.loads(request.body)
    newPassword = data["newPassword"]
    user = request.user
    user.set_password(newPassword)
    user.save()
    
    #Change Token
    Token.objects.delete(user=user)
    token = Token.objects.create(user=user)
    return Response({"Token": token})

class TokenChk(APIView):
  def post(self, request):
    user = request.user
    token = Token.objects.get(user=user)
    if (token is None):
      return Response({"Access Denied"})
    return Response(status=200)

class Chk(APIView):
  def get(self, request):
    print(request.user)
    print(request.auth)
    chk = User.objects.all()
    serializer = UserSerializer(chk, many=True)
    return Response(serializer.data)