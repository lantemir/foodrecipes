# from urllib import response
from datetime import datetime
from distutils.log import error
from email.mime import base
from pyexpat import model
from random import random
import time
from django.shortcuts import render
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from . import models
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import random
import base64
from django.utils import timezone
# Create your views here.



def index(request):
    context = {}

    return render(request, 'index.html', context)


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
@csrf_exempt
def login(request):
    if request.method == "POST":
        userLogin = request.POST.get("userLogin", None)
        password = request.POST.get("password", None)

       
      
        if userLogin and password:
            user = authenticate(username=userLogin, password=password)
            serialized_user = serializers.UserSerializer(instance=user, many= False).data


            print("useeeer")
            print(user)
            print(serialized_user)
            print("useeeer")
            
            password = ''
            for i in range(1, 32+1): 
                password += random.choice('qwertyuiopadfghjklzxcvbnm123456789')

            print(password)

            encoded_password = base64.b64encode(password.encode())[0:-1:1]
            print(encoded_password)

            try:
                print("tryyyyyyy")
                token = models.ModelToken.objects.get(
                    user=user
                )
                print(token)
                print("tryyyyyyy")
                token.token = encoded_password.decode()
                token.datetime_field = timezone.now()
                token.save()
            except Exception as error:
                print("exceeeeeeeeeeept")
                token = models.ModelToken.objects.create(
                    user=user,
                    token=encoded_password.decode()
                )
            print(token)
            serialized_token = serializers.ModelTokenSerializer(instance=token, many= False).data

            print(f"serialized_token:  {serialized_token}")
            return Response(serialized_token, status=status.HTTP_200_OK)
            # print (user)
            # print (serialized_user) 
            # if user:
            #     print ("succces")
            # else: 
            #     print("fail")
            # return JsonResponse({"response": serialized_user }, safe=False)
        else:
            return HttpResponse(status= 404)
    else:
        return HttpResponse(stattus= 405)



@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])
@csrf_exempt
def get_users(request):
    if request.method == "POST":  # create
        pass
    if request.method == "GET":  # read one object / read list of objects
        pass
    if request.method == "PUT":  # update
        pass
    if request.method == "DELETE":  # delete
        pass


    # print("aaaaaaaaaaaaaaaaaaaaaaaaaaa")

    # chats_db =  models.Chat_model.objects.all()



    # serialized_chat= serializers.ModelChatSerializer(instance=chats_db, many=True).data  

    # print(serialized_chat)

    
    token = str(request.META.get("HTTP_AUTHORIZATION", "Bearer $")).split("Bearer ")[1].strip()
    print(f"token: {token}\n")
    # return Response({"usersdb": serialized_chat, "status": status.HTTP_200_OK})




    try:
        token_obj = models.ModelToken.objects.get(token=token)
        
       
        user = token_obj.user

        if user:
            print(f"user from token: {user}")
            users_from_db = User.objects.all()
            serialized_users = serializers.AllUserSerializer(instance=users_from_db, many=True).data #json
            # возвращаем данные через DRF
            return Response({"usersdb": serialized_users, "status": status.HTTP_200_OK})

        else:
            return Response( status.HTTP_401_UNAUTHORIZED)
        
    except Exception as error:
        print(f"error: {error}")
        return Response( status.HTTP_401_UNAUTHORIZED)


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
@csrf_exempt
def get_stories(request):

   # time.sleep(3) # для имитации задержки ответа

    if request.method == "GET":     

        currentPage = int(request.GET.get("currentPage", 1))
        pageSize = int(request.GET.get("pageSize", 8))

        # print(f"pageSize: {pageSize}")

        stories_from_db = models.Story.objects.all()
        stories_count = models.Story.objects.all().count()
        serialized_stories = serializers.StorySerializer(instance=stories_from_db, many=True).data   

        paginator_obj = Paginator(serialized_stories, pageSize)

        current_page = paginator_obj.get_page(currentPage).object_list
 
        return Response({"stories_count": stories_count, "current_page": current_page})
      

        # return Response({"storiesdb": serialized_stories, "current_page": current_page})


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
@csrf_exempt
def get_words(request):
    if request.method == "GET":
        
        words_from_db = models.New_word_story.objects.all()      

        serialized_stories = serializers.WordSerializer(instance=words_from_db, many=True).data       

        return Response({"wordsdb": serialized_stories})



@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
@csrf_exempt
def get_story_by_id(request, story_id):
  
    if request.method == "GET":
        story_by_id = models.Story.objects.get(pk = story_id)
   
        serialized_story_by_id = serializers.StoryByIdSerializer(instance=story_by_id, many=False).data
       
        return Response({"storyByIdDb": serialized_story_by_id})


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
@csrf_exempt
def lobby(request):
  
    if request.method == "GET":
        
       
        return Response({"status": "ok"})

        



