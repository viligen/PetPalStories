# Generated by Django 4.1.3 on 2022-11-09 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_story_model'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'verbose_name_plural': 'Stories'},
        ),
    ]
