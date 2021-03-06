from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import * 

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
