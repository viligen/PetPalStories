# Generated by Django 4.1.3 on 2022-11-09 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_alter_story_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
