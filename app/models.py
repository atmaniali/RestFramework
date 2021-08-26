from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
# Create your models here.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

