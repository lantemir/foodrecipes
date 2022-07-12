from django.urls import path
from app_foodrecipes import views

urlpatterns = [    
    path(route='api/get_users/', view=views.get_users),
]