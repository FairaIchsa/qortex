from rest_framework.viewsets import ModelViewSet

from mainapp.api.singer.serializers import SingerModelSerializer
from ..models import Singer


class SingerModelViewset(ModelViewSet):
    queryset = Singer.objects.all()

    def get_serializer_class(self):
        if self.request == "GET":
            print("Hi there")
            return SingerModelSerializer



#
#
# class SongModelViewset(ModelViewSet):
#     queryset = Song.objects.all()
#     serializer_class = SongModelSerializer
