# Generated by Django 4.1.3 on 2022-11-29 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_alter_post_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_parent',
            new_name='parent_post',
        ),
    ]
