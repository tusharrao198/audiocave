from music_room.models import Room
from rest_framework import routers, serializers, viewsets


class UpdateroomSerializer(serializers.ModelSerializer):
    # code = serializers.CharField(validators=[])
    is_playing = serializers.BooleanField(validators=[])

    class Meta:
        model = Room
        fields = ["code", "is_playing"]
