# Generated by Django 4.1.3 on 2022-12-01 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stories', '0006_alter_story_image'),
        ('common', '0013_alter_signedpetition_is_agreed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagestory',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='messagestory',
            name='story',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stories.story'),
        ),
    ]
