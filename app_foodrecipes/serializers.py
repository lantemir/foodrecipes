from dataclasses import fields
from django.contrib.auth.models import User
from django.urls import clear_script_prefix
from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer): # сериализатор(конвертер данные в JSON)

    class Meta:
        model = User
        fields = '__all__'