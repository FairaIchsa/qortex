from rest_framework import serializers

from ..models import Singer, Album, Song


class SingerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = '__all__'


class AlbumModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'singer', 'name', 'songs']
        depth = 1


class SongModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
