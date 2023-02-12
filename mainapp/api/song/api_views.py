from rest_framework.viewsets import ModelViewSet

from .serializers import SongListModelSerializer, SongRetrieveModelSerializer, SongCreateUpdateSerializer
from ...models import Song


class SingerModelViewset(ModelViewSet):
    queryset = Song.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return SongListModelSerializer
        if self.action == 'retrieve':
            return SongRetrieveModelSerializer
        if self.action == 'create' or self.action == 'update':
            return SongCreateUpdateSerializer
