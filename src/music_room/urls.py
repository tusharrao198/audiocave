from django.urls import path

from . import views
from .views import (
    RoomView,
    CreateRoomView,
    GetRoomView,
    JoinRoomView,
    # UserinRoomView,
    UserLeaveRoomView,
)

urlpatterns = [
    # path("", views.music_room, name="music-home"),
    path("api/", RoomView.as_view(), name="music-api"),
    path("api/createroom/", CreateRoomView.as_view(), name="create-room-api"),
    path("api/getroom/<str:code>/", views.GetRoomView, name="getroom-api"),
    path("api/joinroom/", views.JoinRoomView, name="joinroom-api"),
    # path("api/userinroom/", views.UserinRoomView, name="userinroom-api"),
    path("api/userleaveroom/", views.UserLeaveRoomView, name="userleaveroom-api"),
]
