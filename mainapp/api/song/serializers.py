from rest_framework.serializers import ModelSerializer, SerializerMethodField, Serializer, \
    CharField, IntegerField, PrimaryKeyRelatedField

from mainapp.models import Singer, Album, Song, Track


class SongSingerSerializer(ModelSerializer):
    class Meta:
        model = Singer
        fields = ['id', 'name']


class SongAlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'year']


class SongListModelSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'singer']

    name = SerializerMethodField()
    singer = SerializerMethodField()

    @staticmethod
    def get_name(obj):
        return obj.song.name

    @staticmethod
    def get_singer(obj):
        return {"id": obj.album.singer.id,
                "name": obj.album.singer.name}


class SongRetrieveModelSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'singer', 'album', 'name']

    name = SerializerMethodField()
    album = SongAlbumSerializer()
    singer = SerializerMethodField()

    @staticmethod
    def get_name(obj):
        return obj.song.name

    @staticmethod
    def get_singer(obj):
        return {"id": obj.album.singer.id,
                "name": obj.album.singer.name}


class SongCreateUpdateSerializer(Serializer):
    album = PrimaryKeyRelatedField(queryset=Album.objects.all())
    song = CharField()
    number = IntegerField()

    def create(self, validated_data):
        song = validated_data.get('song')
        album = validated_data.get('album')
        number = validated_data.get('number')

        if not Track.objects.filter(name=song):
            Track.objects.create(name=song)
        song = Track.objects.get(name=song)

        return Song.objects.create(song=song, album=album, number=number)

    def update(self, instance, validated_data):
        song = validated_data.get('song')
        instance.album = validated_data.get('album')
        instance.number = validated_data.get('number')

        if not Track.objects.filter(name=song):
            Track.objects.create(name=song)
        instance.song = Track.objects.get(name=song)

        return instance
