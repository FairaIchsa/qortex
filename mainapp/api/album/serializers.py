from rest_framework.serializers import ModelSerializer, SerializerMethodField

from mainapp.models import Album, Song


class AlbumListModelSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'singer', 'name']

    singer = SerializerMethodField()

    @staticmethod
    def get_singer(obj):
        return obj.singer.name


class AlbumSongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = ['number', 'name']

    name = SerializerMethodField()

    @staticmethod
    def get_name(obj):
        return obj.song.name


class AlbumRetrieveModelSerializer(AlbumListModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'singer', 'name', 'songs']

    singer = SerializerMethodField()
    songs = AlbumSongSerializer(many=True)

    @staticmethod
    def get_singer(obj):
        return obj.singer.name
