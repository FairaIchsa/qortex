from rest_framework.viewsets import ModelViewSet

from .serializers import AlbumListModelSerializer, AlbumRetrieveModelSerializer
from ...models import Album


class AlbumModelViewset(ModelViewSet):
    queryset = Album.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AlbumListModelSerializer
        if self.action == 'retrieve':
            return AlbumRetrieveModelSerializer
