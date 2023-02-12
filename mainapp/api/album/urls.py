from django.urls import path

from .api_views import AlbumModelViewset


app_name = 'album'

urlpatterns = [
    path('', AlbumModelViewset.as_view({'get': 'list'})),
    path('<int:pk>', AlbumModelViewset.as_view({'get': 'retrieve'})),
    path('<int:pk>/update', AlbumModelViewset.as_view({'put': 'update'})),
    path('<int:pk>/delete', AlbumModelViewset.as_view({'delete': 'destroy'})),
    path('add/', AlbumModelViewset.as_view({'post': 'create'})),
]
