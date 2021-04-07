from django.db import models
import random
import string


def generate_room_code():
    length_ = 6
    while True:
        code_ = "".join(random.choices(string.ascii_uppercase, k=length_))
        if Room.objects.filter(code=code_).count() == 0:
            break
    return code_

url_ = "https://www.youtube.com/watch?v=CtUIXnJKPgU"

class Room(models.Model):
    code = models.CharField(default=generate_room_code, max_length=50, unique=True, primary_key=True)
    host = models.CharField(unique=True, max_length=50)
    ishost = models.BooleanField(default=False)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_count_to_skip = models.IntegerField(null=False, default=1)
    current_song = models.CharField(max_length=100, null=True)
    is_playing = models.BooleanField(default=False)
    songurl = models.CharField(default=url_, max_length=1999)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ROOM CODE = {self.code}"
