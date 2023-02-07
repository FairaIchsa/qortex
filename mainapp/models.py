from django.db import models


class Track(models.Model):
    name = models.CharField(max_length=255)


class Singer(models.Model):
    name = models.CharField(max_length=255)


class Album(models.Model):
    singer = models.ForeignKey(Singer, related_name='albums', on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField()


class Song(models.Model):
    song = models.ForeignKey(Track, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField()

