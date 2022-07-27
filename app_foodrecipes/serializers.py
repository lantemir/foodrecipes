from dataclasses import fields
from django.contrib.auth.models import User
from django.urls import clear_script_prefix
from rest_framework import serializers
from . import models
import base64

class UserSerializer(serializers.ModelSerializer): # сериализатор(конвертер данные в JSON)

    class Meta:
        model = User
        fields = '__all__'


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Story
        fields = '__all__'

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.New_word_story
        fields = '__all__'

class StoryByIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Story
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    token =serializers.SerializerMethodField(read_only= True)
    fullname =serializers.SerializerMethodField(read_only= True)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['token', 'usernam','fullname', 'password']
    def get_token(self, obj):
        try:
            return str(obj.username).encode()
        except Exception as error:
            return None

    def get_fullname(self, obj):
        try:
            return f"{obj.first_name}"
        except Exception as error:
            return None