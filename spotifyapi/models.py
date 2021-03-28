from django.db import models
from music_room.models import Room
class Spotifytoken(models.Model):
    user_id = models.CharField(max_length=500, unique=True)
    refresh_token = models.CharField(max_length=500)
    access_token = models.CharField(max_length=500)
    expires_in = models.CharField(max_length=50)
    token_type = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"USER_ID = {self.user_id}"

class Votecount(models.Model):
    user_id = models.CharField(max_length=500, unique=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    song_id = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Votes = {self.user_id}"
