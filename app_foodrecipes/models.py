from django.db import models
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator #проверки валидации
from django.contrib.auth.models import User

# Create your models here.


class StoryCategory(models.Model): 
    title = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="заголовок",
        verbose_name="Заголовок",
        help_text='<small class="text-muted">это наш заголовок</small><hr><br>',
        max_length=250,
    )

    class Meta:
        app_label = 'app_foodrecipes' # для отображения в админке и ещё надо изменить и добавить в apps.py
        # ordering = ('title') # сортировка сначала по title потом по dexcription
        verbose_name = 'Категория'    
        verbose_name_plural = 'Категории историй'

    def __str__(self) -> str:
        return f'{self.title}'


class Story(models.Model): 
    title = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="заголовок",
        verbose_name="Заголовок",
        help_text='<small class="text-muted">это наш заголовок</small><hr><br>',
        max_length=250
    )

    image = models.ImageField(       
        unique=False,
        editable=True,
        blank=True, #отображение в модельке админ
        null=True,
        default="img/story/default/redefault_story.jpg",
        verbose_name="Заставка:",
        help_text='<small class="text-muted">это наш заставка</small><hr><br>',
        
        validators=[FileExtensionValidator(['jpg', 'png'])],
        max_length=100,
    )

    time_to_learn = models.IntegerField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="1",
        verbose_name="Время на учёбу (минут)",
        help_text='<small class="text-muted">это наш время на учёбу</small><hr><br>',

        validators=[MinValueValidator(1), MaxValueValidator(9999)],
    )

    category = models.ForeignKey(  # ссылается на категорию как бы без категории не может быть истории. Сначала создаём историю БД, потом ссылаемся на категорию. 
        error_messages=False,
        primary_key=False,
        unique_for_date=False,
        unique_for_month=False,
        unique_for_year=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default= None,
        verbose_name="Категория",
        help_text='<small class="text-muted">Категория</small><hr><br>',

        to=StoryCategory,
        on_delete=models.SET_NULL, #CASCADE SET_NULL DO_NOTHING
       
    )

    description = models.TextField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True, #можно оставить пустым
        null=True,
        default="Описание",
        verbose_name="Описание",
        help_text='<small class="text-muted">это наш заголовок</small><hr><br>',
    )

    class Meta:
        app_label = 'app_foodrecipes' # для отображения в админке и ещё надо изменить и добавить в apps.py
      # ordering = ('-title') # сортировка сначала по title потом по dexcription
        verbose_name = 'История'    
        verbose_name_plural = 'Истории'

    def __str__(self) -> str: # возвращает строковое представление объекта (в админке)
        return f'{self.title}' 

    def return_clear_data(self):
        title = self.title
        return str(title).strip()



class StoryRaiting(models.Model):
    rating_value = models.IntegerField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="0",
        verbose_name="Оценка",
        help_text='<small class="text-muted">Оценка</small><hr><br>',

        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    user = models.ForeignKey(        
        error_messages=False,
        primary_key=False,
        unique_for_date=False,
        unique_for_month=False,
        unique_for_year=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default= None,
        verbose_name="История",
        help_text='<small class="text-muted">История</small><hr><br>',

        to=User,
        on_delete=models.SET_NULL, #CASCADE SET_NULL DO_NOTHING
       
    )

    story = models.ForeignKey(
        error_messages=False,
        primary_key=False,
        unique_for_date=False,
        unique_for_month=False,
        unique_for_year=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default= None,
        verbose_name="История",
        help_text='<small class="text-muted">История</small><hr><br>',

        to=Story,
        on_delete=models.SET_NULL, #CASCADE SET_NULL DO_NOTHING
       
    )

    class Meta:
        app_label = 'app_foodrecipes' # для отображения в админке и ещё надо изменить и добавить в apps.py
        # ordering = ('title') # сортировка сначала по title потом по dexcription
        verbose_name = 'Рейтинг истории'    
        verbose_name_plural = 'Рейтинг историй'

    def __str__(self) -> str:
        return f'{self.story}'  



class StoryComment(models.Model):
    comment_text = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="Текст комментарий",
        verbose_name="Заголовок",
        help_text='<small class="text-muted">тексь комментария</small><hr><br>',
        max_length=500,
    )

    user = models.ForeignKey(        
        error_messages=False,
        primary_key=False,
        unique_for_date=False,
        unique_for_month=False,
        unique_for_year=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default= None,
        verbose_name="Пользователь",
        help_text='<small class="text-muted">История</small><hr><br>',

        to=User,
        on_delete=models.SET_NULL, #CASCADE SET_NULL DO_NOTHING
       
    )

    story = models.ForeignKey(
        error_messages=False,
        primary_key=False,
        unique_for_date=False,
        unique_for_month=False,
        unique_for_year=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default= None,
        verbose_name="История",
        help_text='<small class="text-muted">История</small><hr><br>',

        to=Story,
        on_delete=models.SET_NULL, #CASCADE SET_NULL DO_NOTHING
       
    )

    class Meta:
        app_label = 'app_foodrecipes' # для отображения в админке и ещё надо изменить и добавить в apps.py
      #  ordering = ('story') # сортировка сначала по title потом по dexcription
        verbose_name = 'Комментарий к истории'    
        verbose_name_plural = 'комментарии к историям'

    def __str__(self) -> str:
        return f'{self.comment_text[:50:1]}' 