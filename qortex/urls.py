from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v1',
      description="API музыкального каталога",
   ),
   public=True,
)

urlpatterns = [
    path('download-api/', schema_view.without_ui(cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('mainapp.urls', namespace='mainapp')),
    path('admin/', admin.site.urls),
]
