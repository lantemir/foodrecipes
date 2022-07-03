from django.apps import AppConfig


class AppFoodrecipesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_foodrecipes'

    verbose_name = 'Банк историй' # для отображения в админке добавить в models.py class Meta: app_label = 'app_foodrecipes' 
