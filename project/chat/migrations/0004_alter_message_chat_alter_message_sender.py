# Generated by Django 4.0.1 on 2022-12-07 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_rename_chatroom_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='chat',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.CharField(max_length=255),
        ),
    ]
