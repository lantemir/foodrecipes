from urllib import response
from django.shortcuts import render

from django.contrib.auth.models import User
from django.http import JsonResponse
from . import models
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from . import serializers
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


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



