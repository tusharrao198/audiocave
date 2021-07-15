from django.urls import path
from . import views
from youtubeapi.views import getYTlink, playpauseSong

urlpatterns = [
    path("getlink/", views.getYTlink, name="getYTlink"),
    path("update/", playpauseSong.as_view(), name="update"),
]
