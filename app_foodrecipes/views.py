# from urllib import response
from django.shortcuts import render
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from . import models
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from . import serializers
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
# Create your views here.


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
@csrf_exempt
def login(request):
    if request.method == "POST":
        userLogin = request.POST.get("userLogin", "")
        password = request.POST.get("password", "")
      
        if userLogin and password:
            user = authenticate(username = userLogin, password = password)
            serialized_user = serializers.UserSerializer(instance=user, many= False).data
            print (user)
            if user:
                print ("succces")
            else: 
                print("fail")
            return JsonResponse({"response": "успешно вошли" }, safe=False)
        else:
            return HttpResponse(status= 404)
    else:
        return HttpResponse(stattus= 405)



@api_view(http_method_names=["GET", "POST"])
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

    users_from_db = User.objects.all()

    serialized_users = serializers.UserSerializer(instance=users_from_db, many=True).data #json

       # возвращаем данные через DRF
    return Response({"usersdb": serialized_users})


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
@csrf_exempt
def get_stories(request):
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

        



