# Generated by Django 4.1.3 on 2022-11-26 11:41

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_alter_story_pet_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
