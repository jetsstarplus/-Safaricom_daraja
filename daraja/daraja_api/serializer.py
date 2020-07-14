from django.contrib.auth.models import User, Group
from django.contrib import admin
admin.autodiscover()

from rest_framework import generics, permissions, serializers

# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )