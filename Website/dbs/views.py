from django.shortcuts import render
from .models import UploadImageTest
from .serializers import ImageSerializer
from rest_framework.generics import ListAPIView
from django.http import HttpResponse
import json

def home(request):
    return HttpResponse("Hello World")

class ImageViewSet(ListAPIView):
    queryset = UploadImageTest.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        name = request.data['name']
        fil = request.data['image']
        image = UploadImageTest.objects.create(name=name,image=fil)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)