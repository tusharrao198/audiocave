from django.shortcuts import render, redirect
import youtube_dl
import json
from decouple import config

from music_room.serializers import RoomSerializer
from .serializers import UpdateroomSerializer


from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from spotifyapi.models import Votecount
from music_room.models import Room

# from youtubeapi.models import Youtubedata
import requests

def getjson(u):
    ydl = {}
    result_ = ""
    count = 1
    for i in range(10):
        print(f"\n\ntrying {count} time\n\n")
        result = youtube_dl.YoutubeDL(ydl).extract_info(u, download=False)
        if result is not None and len(result) != 0:
            result_ = result
            break
        else:
            count += 1
    formats = result_["formats"]
    # votes = Votecount.objects.filter(room=room, song_id=result["id"])
    song_info = {
        "song_id": result_["id"],
        "song_name": result_["title"],
        "artist": result_["creator"],
        "image_url": result_["thumbnails"][3]["url"],
        "duration": result_["duration"],
        "view_count": result_["view_count"],
        # "vote": len(votes),
        # "votes_required": room.votes_count_to_skip,
    }
    for i in formats:
        f = i["format"]
        if "audio only" in f:
            song_info["song_url"] = i["url"]
            break
    return song_info


@api_view(["GET", "POST"])
def getYTlink(request, *args, **kwargs):
    roomCode = request.session.get("Room_code")
    room = Room.objects.filter(code=roomCode)
    if room.exists():
        room = room[0]
    else:
        return Response(
            {"BAD REQUEST": "ROOM NOT FOUND"}, status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "POST":
        lookup_url_kwargs = "ytlink"
        url_ = request.data.get(lookup_url_kwargs)
        print("post youtube url", url_)
        ydl = {}
        if url_ is None:
            url_ = "https://www.youtube.com/watch?v=_NGQfFCFUn4"
            # url_ = room.songurl
        result = ""
        for i in range(10):
            result_ = youtube_dl.YoutubeDL(ydl).extract_info(url_, download=False)
            if result_ is not None and len(result_) != 0:
                result = result_
                break
        try:
            formats = result["formats"]
            # votes = Votecount.objects.filter(room=room, song_id=result["id"])
            # print(f"votes = {votes} ")
            song_info = {
                "song_id": result["id"],
                "song_name": result["title"],
                "artist": result["creator"],
                "image_url": result["thumbnails"][3]["url"],
                "duration": result["duration"],
                "view_count": result["view_count"],
                # "vote": len(votes),
                # "votes_required": room.votes_count_to_skip,
            }
            for i in formats:
                f = i["format"]
                if "audio only" in f:
                    song_info["song_url"] = i["url"]
                    break
                else:
                    print("NO AUDIO FOUND")
            print("working 1")
            if room.current_song != song_info["song_id"]:
                print("working 2")
                room.current_song = song_info["song_id"]
                try:
                    if len(url_) !=0 and url_ is not None:
                        print("working 3")
                        room.songurl = url_
                        room.save(update_fields=["current_song", "songurl"])
                except:
                    print("working 4")
                    room.save(update_fields=["current_song"])
                # votes = Votecount.objects.filter(room=room.code).delete()
                print("working 5")
            return Response(song_info, status=status.HTTP_200_OK)
        except:
            print("ERROR CONNECTION")
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == "GET":
        print("room, song url", room.songurl)
        song_data = getjson(room.songurl)
        print("\n   ",song_data, "\n\n")
        song_info = {
            "song_id": song_data["song_id"],
            "song_name": song_data["song_name"],
            "artist": song_data["artist"],
            "image_url": song_data["image_url"],
            # "duration": "dur",
            # "view_count": "def",
            # "vote": "def",
            # "votes_required": room.votes_count_to_skip,
            "song_url": song_data["song_url"],
        }
        return Response(song_info, status=status.HTTP_200_OK)


class playpauseSong(UpdateAPIView):
    serializer_class = UpdateroomSerializer
    print("UpdateroomView called")

    def patch(self, request, format=None):
        serializer = self.serializer_class(
            data=request.data
        )  # getting data from post request made on the endpoint
        print(f"UpdateRoomView = {serializer}")

        if serializer.is_valid():
            print("HELLO")
            # q = json.loads(serializer.data)
            # print(type(q), q)
            is_playing = serializer.data.get("is_playing")  # getting data from api view
            # code = serializer.data.get("roomCode")
            code = request.data["roomCode"]
            print("CODE", code)
            if code == self.request.session.get("Room_code"):
                queryset = Room.objects.filter(code=code)
                print(f"qqqqq = {queryset}")
                if not queryset.exists():
                    return Response(
                        {"msg": "Room not found."}, status=status.HTTP_404_NOT_FOUND
                    )
                print("ROOM")
                room = queryset[0]
                user_id = self.request.session.session_key
                if room.host == user_id or room.guest_can_pause:
                    room.is_playing = is_playing
                    room.save(update_fields=["is_playing"])
                    return Response(
                        RoomSerializer(room).data, status=status.HTTP_200_OK
                    )
        print(serializer.errors)
        return Response({}, status=status.HTTP_403_FORBIDDEN)



# def play_pause_Song(session_key):
#     # print("playsong called",session_key)
#     endpoint = "player/play"
#     return execute_SpotifyAPIrequest(session_key, endpoint, put_=True)


# @api_view(["PUT", "PATCH"])
# def playpauseSong(request):
#     serializer_class = UpdateroomSerializer
#     print("UpdateRoomView called")
#     serializer = serializer_class(
#         data=request.data
#     )  # getting data from post request made on the endpoint

#     print(f"UpdateRoomView = {serializer}")

#     if serializer.is_valid():
#         is_playing = serializer.data.get("is_playing")  # getting data from api view
#         code = serializer.data.get("roomCode")
#         if code == request.session.get("Room_code"):
#             queryset = Room.objects.filter(code=code)
#             print(f"qqqqq = {queryset}")
#             if not queryset.exists():
#                 return Response(
#                     {"msg": "Room not found."}, status=status.HTTP_404_NOT_FOUND
#                 )
#             room = queryset[0]
#             user_id = request.session.session_key
#             if room.host == user_id or room.guest_can_pause:
#                 room.is_playing = is_playing
#                 room.code = code
#                 room.save(update_fields=["is_playing", "code"])
#                 return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
#     print(serializer.errors)
#     return Response({}, status=status.HTTP_403_FORBIDDEN)
