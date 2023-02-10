from rest_framework.viewsets import ModelViewSet

from .serializers import SingerModelSerializer, AlbumModelSerializer, SongModelSerializer
from ..models import Singer, Album, Song


class SingerModelViewset(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerModelSerializer


class AlbumModelViewset(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer


class SongModelViewset(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongModelSerializer
