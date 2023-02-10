from django.db import models


class Track(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"({self.id}) {self.name}"


class Singer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Album(models.Model):
    name = models.CharField(max_length=255)
    singer = models.ForeignKey(Singer, related_name='albums', on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.name} - {self.singer}"


class Song(models.Model):
    song = models.ForeignKey(Track, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.number}.{self.song.name} ({self.album})"

