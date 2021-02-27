from django.contrib import admin
from django.urls import path, include
from music_room import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("music_room.urls")),
    path("spotify/", include("spotifyapi.urls")),
    path("youtube/", include("youtubeapi.urls")),
    path("chat/", include("chatroom.urls")),
    path("", TemplateView.as_view(template_name="index.html"), name="App.js"),
    path("homepage/", TemplateView.as_view(template_name="index.html")),
    path("room/", TemplateView.as_view(template_name="index.html")),
    path("joinroom/", TemplateView.as_view(template_name="index.html")),
    path("createroom/", TemplateView.as_view(template_name="index.html")),
    path("room/<str:roomCode>/", TemplateView.as_view(template_name="index.html")),
    # path("joinroom/<str:roomCode>/", TemplateView.as_view(template_name="index.html")),
    path("notfound/", TemplateView.as_view(template_name="index.html")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
