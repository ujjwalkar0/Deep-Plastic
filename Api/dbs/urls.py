from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ImageViewSet, home

urlpatterns = [
    path('upload/', ImageViewSet.as_view(), name='upload'),
    path('', home, name='upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)