# Generated by Django 3.2.5 on 2021-07-15 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_room', '0004_alter_room_songurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='songurl',
            field=models.CharField(default='1lRGr4rSCz4', max_length=1999),
        ),
    ]
