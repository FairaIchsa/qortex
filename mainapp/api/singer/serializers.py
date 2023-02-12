from rest_framework.serializers import ModelSerializer

from mainapp.models import Singer, Album


class SingerListModelSerializer(ModelSerializer):
    class Meta:
        model = Singer
        fields = ['id', 'name']


class SingerAlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'year']


class SingerRetrieveModelSerializer(ModelSerializer):
    class Meta:
        model = Singer
        fields = ['id', 'name', 'albums']

    albums = SingerAlbumSerializer(many=True)


class SingerCreateUpdateModelSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = ['name']
