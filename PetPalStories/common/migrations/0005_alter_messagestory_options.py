# Generated by Django 4.1.3 on 2022-11-16 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_rename_favourite_favouritestory_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messagestory',
            options={'ordering': ('-sent_on',)},
        ),
    ]
