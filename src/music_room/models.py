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


class Room(models.Model):
    code = models.CharField(default=generate_room_code, max_length=50, unique=True)
    host = models.CharField(unique=True, max_length=50)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_count_to_skip = models.IntegerField(null=False, default=1)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ROOM CODE = {self.code}"
