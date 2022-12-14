# Generated by Django 4.1.3 on 2022-12-02 10:34

import PetPalStories.core.validators
import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0006_alter_story_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, validators=[PetPalStories.core.validators.validate_image_size], verbose_name='image'),
        ),
    ]
