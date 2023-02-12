from rest_framework.viewsets import ModelViewSet

from .serializers import SingerListModelSerializer, SingerRetrieveModelSerializer, SingerCreateUpdateModelSerializer
from ...models import Singer


class SingerModelViewset(ModelViewSet):
    queryset = Singer.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return SingerListModelSerializer
        if self.action == 'retrieve':
            return SingerRetrieveModelSerializer
        if self.action == 'create' or self.action == 'update':
            return SingerCreateUpdateModelSerializer
