from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.shortcuts import redirect

urlpatterns = [
    path('', ViewData.as_view(), name='home'),
    path('daily/', DailyStat.as_view()),
    path('daily/<str:loc>/', DailyStat.as_view()),
    path('location/', LocationStat.as_view()),
    path('location/<str:date>', LocationStat.as_view()),
    path('get_token/', GetTokenView.as_view()),
    path('accounts/profile/', lambda x: redirect('/', permanent=True)),
    path('login/',UserLoginView.as_view(),name="login"),
    path('api/', ImageViewSet.as_view(), name='api'),
    path('upload/', Uploader, name='upload'),
    # path('link/<str:a>/<str:b>/<str:c>',ObjectDetect, name='link'),
    path('<str:pk>/',ViewByDate,name='ViewByDate'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
