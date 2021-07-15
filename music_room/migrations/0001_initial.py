# Generated by Django 3.2.5 on 2021-07-15 15:05

from django.db import migrations, models
import music_room.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('code', models.CharField(default=music_room.models.generate_room_code, max_length=50, primary_key=True, serialize=False, unique=True)),
                ('host', models.CharField(max_length=50, unique=True)),
                ('ishost', models.BooleanField(default=False)),
                ('guest_can_pause', models.BooleanField(default=False)),
                ('votes_count_to_skip', models.IntegerField(default=1)),
                ('current_song', models.CharField(max_length=100, null=True)),
                ('is_playing', models.BooleanField(default=False)),
                ('songurl', models.CharField(default='9-rKvhsjwKU', max_length=1999)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
