# Generated by Django 4.0.4 on 2022-07-03 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_foodrecipes', '0005_story_author_alter_storycomment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='New_word_story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(blank=True, default='новое слово', help_text='<small class="text-muted">это новое слово</small><hr><br>', max_length=50, null=True, verbose_name='новое слово')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории историй',
            },
        ),
    ]
