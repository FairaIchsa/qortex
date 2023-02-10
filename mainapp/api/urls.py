from rest_framework.routers import DefaultRouter

from .api_views import SingerModelViewset, AlbumModelViewset, SongModelViewset

app_name = 'api'

router = DefaultRouter()
router.register(r'singer', SingerModelViewset, basename='singer')
router.register(r'album', AlbumModelViewset, basename='album')
router.register(r'song', SongModelViewset, basename='song')

urlpatterns = router.urls
