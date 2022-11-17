# Generated by Django 4.1.3 on 2022-11-16 09:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_story_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0003_rename_owner_message_sender'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Favourite',
            new_name='FavouriteStory',
        ),
        migrations.RenameModel(
            old_name='Message',
            new_name='MessageStory',
        ),
    ]