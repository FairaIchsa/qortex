from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('singer/', include('mainapp.api.singer.urls', namespace='singer')),
    path('album/', include('mainapp.api.album.urls', namespace='album')),
    path('song/', include('mainapp.api.song.urls', namespace='song')),
]
