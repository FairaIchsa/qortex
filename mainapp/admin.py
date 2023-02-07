from django.contrib import admin

from mainapp.models import Track, Song, Album, Singer


admin.site.register(Track)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Singer)
