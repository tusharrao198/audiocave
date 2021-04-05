from django.shortcuts import render, redirect
from django.db import models
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from .models import Room
from .serializers import RoomSerializer, CreateRoomSerializer, UpdateRoomSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

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
            self.request.session.create()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.get("guest_can_pause")
            votes_count_to_skip = serializer.data.get("votes_count_to_skip")
            ishost = True
            host = self.request.session.session_key
            queryset = Room.objects.filter(host=host)
            if queryset.exists():
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_count_to_skip = votes_count_to_skip
                room.ishost = ishost
                room.save(
                    update_fields=["guest_can_pause", "votes_count_to_skip", "ishost"]
                )
                request.session["Room_code"] = room.code
            else:
                room = Room(
                    host=host,
                    ishost=ishost,
                    guest_can_pause=guest_can_pause,
                    votes_count_to_skip=votes_count_to_skip,
                )
                room.save()
                request.session["Room_code"] = room.code
            return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateRoomView(UpdateAPIView):
    serializer_class = UpdateRoomSerializer

    def patch(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(
            data=request.data
        )  # getting data from post request made on the endpoint

        if serializer.is_valid():
            guest_can_pause = serializer.data.get(
                "guest_can_pause"
            )  # getting data from api view
            votes_count_to_skip = serializer.data.get("votes_count_to_skip")
            code = serializer.data.get("code")
            queryset = Room.objects.filter(code=code)
            if not queryset.exists():
                return Response(
                    {"msg": "Room not found."}, status=status.HTTP_404_NOT_FOUND
                )
            room = queryset[0]
            # print(f"UpdateRoomView room = {room}")
            user_id = self.request.session.session_key
            # print(f"room host = {room.host}, and user_id={user_id}")
            if room.host != user_id:
                return Response(
                    {"msg": "You are not the host of this room."},
                    status=status.HTTP_403_FORBIDDEN,
                )
            room.guest_can_pause = guest_can_pause
            room.votes_count_to_skip = votes_count_to_skip
            room.save(update_fields=["guest_can_pause", "votes_count_to_skip"])
            return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
        return Response(
            {"Bad Request": "Invalid Data..."}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST"])
def JoinRoomView(request, *args, **kwargs):
    lookup_url_kwargs = "code"
    # is the name that is sent as post request from room page in react
    if not request.session.exists(request.session.session_key):
        request.session.create()
    code = request.data.get(lookup_url_kwargs)
    print("Joining CODE", code)
    queryset = Room.objects.filter(code=code)
    if queryset is not None:
        room = queryset[0]
        request.session["Room_code"] = code
        return Response({"message": "Room Joined"}, status=status.HTTP_200_OK)

    return Response(
        {"Bad Request": "Room not found/Invalid Room Code"},
        status=status.HTTP_404_NOT_FOUND,
    )


@api_view(["POST"])
def UserLeaveRoomView(request):
    if "Room_code" in request.session:
        host_id = request.session.session_key
        room = Room.objects.filter(host=host_id)
        if len(room) > 0:
            room[0].delete()
        return Response({"Message": "SUCCESS"}, status=status.HTTP_200_OK)
    return Response(
        {"BAD REQUEST": "USER/You ALREADY LEFT"}, status=status.HTTP_404_NOT_FOUND
    )


@api_view(["GET"])
def UserinRoomView(request):
    if not request.session.exists(request.session.session_key):
        request.session.create()
        print("CREATING IN USERIN ROOM VIEW")
    code = request.session.get("Room_code")
    print(f"Userinroom view called and code= {code}")
    queryset = Room.objects.filter(code=code)
    return JsonResponse({"code": code}, status=status.HTTP_200_OK)


@api_view(["GET"])
def GetRoomView(request, code):  # this core parameter coming from url
    if request.session.get("Room_code") == code:
        queryset = Room.objects.filter(code=code)
        if queryset.exists():
            data = RoomSerializer(queryset[0]).data
            data["RoomCodeinSession"] = code
            data["ishost"] = (
                request.session.session_key == queryset[0].host
            )  # added extra field to send data to react
            serializer = RoomSerializer(queryset, many=True)
            return Response(data, status=status.HTTP_200_OK)
        else:
            print("ELSE POP", request.session.pop("Room_code"))
            print("Deleting Session")
            request.session.delete()
            print("Deleted Session")
    print("ROOM NOT FOUND IN GETROOMVIEW")
    return Response(
        {"BAD REQUEST": "ROOM LEFT BY USER"}, status=status.HTTP_404_NOT_FOUND
    )
