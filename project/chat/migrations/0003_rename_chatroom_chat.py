# Generated by Django 4.0.1 on 2022-12-07 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_remove_chatroom_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChatRoom',
            new_name='Chat',
        ),
    ]
