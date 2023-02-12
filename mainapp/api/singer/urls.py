from django.urls import path

from .api_views import SingerModelViewset


app_name = 'singer'

urlpatterns = [
    path('', SingerModelViewset.as_view({'get': 'list'})),
    path('<int:pk>', SingerModelViewset.as_view({'get': 'retrieve'})),
    path('<int:pk>/update', SingerModelViewset.as_view({'put': 'update'})),
    path('<int:pk>/delete', SingerModelViewset.as_view({'delete': 'destroy'})),
    path('add/', SingerModelViewset.as_view({'post': 'create'})),
]
