# Generated by Django 4.1.3 on 2022-12-02 10:56

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petitions', '0006_alter_petition_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petition',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
