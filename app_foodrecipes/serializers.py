from dataclasses import fields
from django.contrib.auth.models import User
from django.urls import clear_script_prefix
from rest_framework import serializers
from . import models
import base64



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
        fields = ['token', 'username','fullname', 'password']
    def get_token(self, obj):
        try:            
            return base64.b64encode(str(obj.username).encode()).decode()
    
        except Exception as error:
            print(error)
            return None

    def get_fullname(self, obj):
        try:
            return f"{obj.first_name} {obj.last_name}"
        except Exception as error:
            print(error)
            return None


class AllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ModelTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelToken
        fields = '__all__'


class ModelChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chat_model       
        fields = '__all__'




   
