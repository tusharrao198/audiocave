from django.contrib import admin
from django.urls import path, include
from music_room import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("music_room.urls")),
    path("youtube/", include("youtubeapi.urls")),
    path("chat/", include("chatroom.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
