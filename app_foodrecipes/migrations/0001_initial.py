# Generated by Django 4.0.4 on 2022-07-03 03:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='заголовок', help_text='<small class="text-muted">это наш заголовок</small><hr><br>', max_length=250, null=True, verbose_name='Заголовок')),
                ('image', models.ImageField(blank=True, default='img/story/default/redefault_story.jpg', help_text='<small class="text-muted">это наш заставка</small><hr><br>', null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])], verbose_name='Заставка:')),
            ],
        ),
    ]