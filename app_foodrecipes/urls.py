from django.urls import path
from app_foodrecipes import views

urlpatterns = [    
    path('', view=views.index, name='index'),

    path(route='api/get_users/', view=views.get_users),

    path(route='api/get_stories/', view=views.get_stories),

    path(route='api/words/', view=views.get_words),

    path(route='api/story_by_id/<story_id>/', view=views.get_story_by_id),

    path(route='login/', view= views.login, name='login'),

    path(route='chat/', view=views.lobby, name='lobby'),


]