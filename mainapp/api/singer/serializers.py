from rest_framework import serializers

from mainapp.models import Singer


class SingerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = '__all__'

