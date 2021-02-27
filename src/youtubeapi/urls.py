from django.urls import path
from . import views
from youtubeapi.views import getYTlink, playpauseSong

urlpatterns = [
    path("getlink/", views.getYTlink, name="YTlink"),
    # path("update/", views.playpauseSong, name="update"),
    path("update/", playpauseSong.as_view(), name="update"),
]
