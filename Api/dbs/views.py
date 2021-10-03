from django.shortcuts import render
from .models import UploadImageTest
from .serializers import ImageSerializer
from rest_framework.generics import ListAPIView
from django.http import HttpResponse
import json
from django.views.generic import ListView #, DeleteView, UpdateView, DetailView, CreateView

def home(request):
    return HttpResponse("Hello World")

class ImageViewSet(ListAPIView):
    queryset = UploadImageTest.objects.all()
    serializer_class = ImageSerializer
    
    def post(self, request, *args, **kwargs):
        name = request.data['name']
        fil = request.data['image']
        location = request.data['location']
        time = request.data['time']
        date = request.data['date']
        print(request.data)        
        image = UploadImageTest.objects.create(name=name,image=fil, location=location,time=time,date=date)

        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)

class ViewData(ListView):
    model = UploadImageTest
    template_name = "home.html"
    ordering = ('-id')

def ViewByDate(request,pk):
    pictures = UploadImageTest.objects.filter(date=pk)
    msg = "Images posted on : "+pk
    if len(pictures)==0:
        msg = "No Image posted on "+pk

    context = {
        'object_list': pictures,
        'photos': msg
    }
    return render(request,'home.html',context)
