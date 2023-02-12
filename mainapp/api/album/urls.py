from django.urls import path, include

from .api_views import AlbumModelViewset


app_name = 'album'

urlpatterns = [
    path('', AlbumModelViewset.as_view({'get': 'list'})),
    path('<int:pk>', AlbumModelViewset.as_view({'get': 'retrieve'}))
]
