from datetime import datetime
from django.contrib import admin

from app_foodrecipes.models import Story, StoryCategory, StoryRaiting, StoryComment, New_word_story, ModelToken

# Register your models here.
# изначально пусто было

# настройка текста для удобства отображение панелей
admin.site.site_header = 'Панель управления приложения'
admin.site.index_title = 'Управления моделями'
admin.site.site_title = 'панель' 

# расширям админу под индивидуальные условия

class StoryAdmin(admin.ModelAdmin):
    list_display =( # поля для отображения
        'title',
        'image',
        'description',       
        'author',
        
    )
    filter_horizontal = ('new_words_story', 'category',) # только для полей флрмата many to many fields
    list_display_links = ( # поля ссылка
        'title',
        'description',       
    )
    list_editable = ( # поля для редактирование объекта на лету
        # 'category',
      
    )
    list_filter = ( 
        'title',
        'image',
        'description',
        
        'author',
       
    )
    fieldsets = ( # подзаголовки для визуального отделения блоков друг от друга
        ('Основное', {'fields': (
            'title',            
            'description',
            'new_words_story',
            'category',
           
        )}),
        ('Дополнительно', {'fields': (
            'image',
            # 'category',
            'author',
        )}),
    )
    search_fields =[ # поле для поиска
        'title',
        'image',
        'description',
        # 'category',
        'author',
        
    ]


class CategortAdmin(admin.ModelAdmin):
    list_display =( # поля для отображения
        'title',      
    )
    list_display_links = ( # поля ссылка
        'title',  
    )
    list_editable = ( # поля для редактирование объекта на лету      
      
    )
    list_filter = ( 
        'title',    
    )
    fieldsets = ( # подзаголовки для визуального отделения блоков друг от друга
        ('Основное', {'fields': (
            'title',           
        )}),
    )
    search_fields =[ # поле для поиска
        'title',
    ]


class New_word_story_Admin(admin.ModelAdmin):
    list_display =( # поля для отображения
        'word',      
    )
    list_display_links = ( # поля ссылка
        'word',  
    )
    list_editable = ( # поля для редактирование объекта на лету      
      
    )
    list_filter = ( 
        'word',    
    )
    fieldsets = ( # подзаголовки для визуального отделения блоков друг от друга
        ('Основное', {'fields': (
            'word',           
        )}),
    )
    search_fields =[ # поле для поиска
        'word',
    ]



class Model_token_Admin(admin.ModelAdmin):
    list_display =( # поля для отображения
        'user',  
        'token',
        'datetime_field',    
    )
    list_display_links = ( # поля ссылка
        'user',  
        'token',
    )
    list_editable = ( # поля для редактирование объекта на лету         
        'datetime_field', 
    )
    list_filter = ( 
        'user',  
        'token',
        'datetime_field', 
    )
    fieldsets = ( # подзаголовки для визуального отделения блоков друг от друга
        ('Основное', {'fields': (
            'user',  
            'token',
            'datetime_field',          
        )}),
    )
    search_fields =[ # поле для поиска
        'word',
    ]





admin.site.register(StoryCategory, CategortAdmin) 
admin.site.register(New_word_story, New_word_story_Admin) 
admin.site.register(Story, StoryAdmin) 
admin.site.register(StoryRaiting) 
admin.site.register(StoryComment) 
admin.site.register(ModelToken, Model_token_Admin) 





