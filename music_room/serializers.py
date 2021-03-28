from .models import Room
from rest_framework import routers, serializers, viewsets


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("guest_can_pause", "votes_count_to_skip", "ishost")


class UpdateRoomSerializer(serializers.ModelSerializer):
    code = serializers.CharField(validators=[])

    class Meta:
        model = Room
        fields = (
            "guest_can_pause",
            "votes_count_to_skip",
            "code",
            "ishost",
        )
