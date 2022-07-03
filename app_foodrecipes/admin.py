from django.contrib import admin

from app_foodrecipes.models import Story, StoryCategory, StoryRaiting, StoryComment

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
        'category',
    )
    list_display_links = ( # поля ссылка
        'title',
        'description',        
    )
    list_editable = ( # поля для редактирование объекта на лету
        'category',
      
    )
    list_filter = ( 
        'title',
        'image',
        'description',
        'category',
    )
    fieldsets = ( # подзаголовки для визуального отделения блоков друг от друга
        ('Основное', {'fields': (
            'title',            
            'description',
        )}),
        ('Дополнительно', {'fields': (
            'image',
            'category',
        )}),
    )
    search_fields =[ # поле для поиска
        'title',
        'image',
        'description',
        'category',
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



admin.site.register(StoryCategory, CategortAdmin) 
admin.site.register(Story, StoryAdmin) 
admin.site.register(StoryRaiting) 
admin.site.register(StoryComment) 





