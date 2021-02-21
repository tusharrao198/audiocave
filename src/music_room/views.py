from django.shortcuts import render
# from django.http import HttpResponse
from django.db import models
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Room
from .serializers import RoomSerializer, CreateRoomSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.http import JsonResponse


class RoomView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class CreateRoomView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = CreateRoomSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            # if not then we create
            self.request.session.create()
        # else
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.get("guest_can_pause")
            votes_count_to_skip = serializer.data.get("votes_count_to_skip")
            host = self.request.session.session_key
            queryset = Room.objects.filter(host=host)
            if queryset.exists():
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_count_to_skip = votes_count_to_skip
                room.save(update_fields=["guest_can_pause", "votes_count_to_skip"])
                request.session["Room_code"] = room.code
            else:
                room = Room(
                    host=host,
                    guest_can_pause=guest_can_pause,
                    votes_count_to_skip=votes_count_to_skip,
                )
                room.save()
                request.session["Room_code"] = room.code
            return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def JoinRoomView(request, *args, **kwargs):
    lookup_url_kwargs = "code"
    # is the name that is sent as post request from room page in react
    if not request.session.exists(request.session.session_key):
        request.session.create()
        print("CREATING IN JOIN ROOM VIEW")
    code = request.data.get(lookup_url_kwargs)
    print("Joining CODE", code)
    queryset = Room.objects.filter(code=code)
    if queryset is not None:
        room = queryset[0]
        request.session["Room_code"] = code
        print(request.session["Room_code"], "IN JOIN ", request.session.session_key)
        return Response({"message": "Room Joined"}, status=status.HTTP_200_OK)

    return Response(
        {"Bad Request": "Room not found/Invalid Room Code"},
        status=status.HTTP_404_NOT_FOUND,
    )


@api_view(["POST"])
def UserLeaveRoomView(request):
    print(f"session_key={request.session.session_key}")
    if "Room_code" in request.session:
        host_id = request.session.session_key
        print(f"hostid= {host_id}")
        room = Room.objects.filter(host=host_id)
        if len(room) > 0:
            print("IF POP", request.session.pop("Room_code"))
            print(f"room= {room}")
            room[0].delete()
        else:
            print("ELSE POP", request.session.pop("Room_code"))
    return Response({"Message": "SUCCESS"}, status=status.HTTP_200_OK)


# @api_view(["GET"])
# def UserinRoomView(request):
#     if not request.session.exists(request.session.session_key):
#         request.session.create()
#         print("CREATING IN USERIN ROOM VIEW")
#     code = request.session.get("Room_code")
#     print("code_sess in userinroom", code)
#     return JsonResponse({"code": code}, status=status.HTTP_200_OK)


@api_view(["GET"])
def GetRoomView(request, code):
    queryset = Room.objects.filter(code=code)
    if queryset is not None:
        data = RoomSerializer(queryset[0]).data
        data["ishost"] = request.session.session_key == queryset[0].host
        serializer = RoomSerializer(queryset, many=True)
        return Response(data, status=status.HTTP_200_OK)

    return Response(
        {"Room not found": "Invalid Room Code"},
        status=status.HTTP_404_NOT_FOUND,
    )
