# Встроенные импорты.
from email import message
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
# from django.contrib.auth.models import User
from django.db import connection


from . import models

from . import serializers





# # Импорты сторонних библиотек.
# from channels.exceptions import DenyConnection
# from channels.generic.websocket import AsyncWebsocketConsumer

# # Импорты Django.
# from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth.models import AnonymousUser

class ChatConsumer(WebsocketConsumer):
    def connect(self):

        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        # self.send(text_data=json.dumps({
        #     'type':'connection_established',
        #     'message': 'you are now connected!'
        # }))

        chats_db =  models.Chat_model.objects.all()

        # app_foodrecipes_chat_model.datetime_field,

      
    

        with connection.cursor() as cursor:
            cursor.execute(''' select app_foodrecipes_chat_model.id, app_foodrecipes_chat_model.photo, 
                app_foodrecipes_chat_model.message,   auth_user.username
                from app_foodrecipes_chat_model
                join auth_user
                on app_foodrecipes_chat_model.user_id = auth_user.id ''')

            columns = [column[0] for column in cursor.description]

            result = []
            
            for row in cursor.fetchall():
                result.append(dict(zip(columns, row)))


            

        print(result) 
            




       

        serialized_chat = serializers.ModelChatSerializer(instance=chats_db, many=True).data  
    


        self.send(text_data=json.dumps({
            'type':'show_chat',
            'message': result
        }))
    


  
    def receive(self, text_data ):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        token = text_data_json["token"]


        token_obj = models.ModelToken.objects.get(token=token)

        user = token_obj.user

        print('token_obj:', token_obj)

        if user:
            models.Chat_model.objects.create(
                user = user,
                message = message
            )

      #  chats_db =  models.Chat_model.objects.all()     

      #  serialized_chat= serializers.ModelChatSerializer(instance=chats_db, many=True).data  



        with connection.cursor() as cursor:
            cursor.execute(''' select app_foodrecipes_chat_model.id, app_foodrecipes_chat_model.photo, 
                app_foodrecipes_chat_model.message,   auth_user.username
                from app_foodrecipes_chat_model
                join auth_user
                on app_foodrecipes_chat_model.user_id = auth_user.id ''')

            columns = [column[0] for column in cursor.description]

            result = []
            
            for row in cursor.fetchall():
                result.append(dict(zip(columns, row)))



        # print('Message: ', message )

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                # 'message': message было
                'message': result
            }
        )

        # self.send(text_data=json.dumps({
        #     'type': 'chat',
        #     'message': message
        # })) 
    
    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))