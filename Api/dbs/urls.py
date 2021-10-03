from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', ViewData.as_view(), name='home'),
    path('home', ViewData.as_view(), name='home'),
    path('api/', ImageViewSet.as_view(), name='api'),
    path('upload/', Uploader, name='upload'),
    path('link/<str:a>/<str:b>/<str:c>',ObjectDetect, name='link'),
    path('<str:pk>/',ViewByDate,name='ViewByDate')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
