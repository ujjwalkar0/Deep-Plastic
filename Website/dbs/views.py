from django.shortcuts import render
from .models import *
from .serializers import ImageSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import json
from django.views.generic import ListView #, DeleteView, UpdateView, DetailView, CreateView
from .forms import *
from .utils import CheckVideo
import os
from django.contrib.auth.views import LoginView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.views import View

class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    redirect_to = "/upload"

class GetTokenView(CreateAPIView, View):
    serializer_class = AuthTokenSerializer

    def get(self, request, *args, **kwargs):    
        token, created = Token.objects.get_or_create(user=request.user)
        return render(request, 'token.html', context={"token": token})

    def post(self, request, *args, **kwargs):
        serializer = ObtainAuthToken.get_serializer(self, data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class ImageViewSet(CreateAPIView):
    serializer_class = ImageSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        fil = request.data['image']
        location = request.user
        print(request.user, fil)
        image = UploadImageTest.objects.create(image=fil, location=location)
        image.save()

        return Response({'message': "Uploaded"}, status=200)

class DailyStat(APIView):
    def get(request, loc, *args, **kwargs):
        print(loc)
        # try:
        #     print(loc)
        #     objects = DailyStatistics.objects.filter(location=loc)
        # except:
        objects = DailyStatistics.objects.all()
    
        daily = {}
        for i in objects:
            if i.date in daily:
                daily[i.date] += i.count
            else:
                daily[i.date] = i.count

        print(daily)

        return Response([{"t":i, "y":daily[i]} for i in daily])

class LocationStat(APIView):
    def get(request, *args, **kwargs):
        objects = DailyStatistics.objects.all()
    
        location = {}
        for i in objects:
            if i.location in location:
                location[i.location.username] += i.count
            else:
                location[i.location.username] = i.count

        print(location)

        return Response([{"t":i, "y":location[i]} for i in location])

        # return Response([{"t":i.location.username, "y":i.count} for i in DailyStatistics.objects.all()])


class ViewData(ListView):
    model = UploadImageTest
    template_name = "home.html"
    ordering = ('-id')


    def get_context_data(self, *args, **kwargs):

        hostname = "http://"+self.request.get_host()
        if self.request.is_secure():
            hostname = "https://"+self.request.get_host()

        context = super(ViewData, self).get_context_data(*args, **kwargs)
        context["date_labels"] = [i.date for i in DailyStatistics.objects.all()]
        context["daily"] = [{i.date, i.count} for i in DailyStatistics.objects.all()]
        context["hostname"] = hostname
        return context

def ViewByDate(request,pk):
    months = ["Jan.", "Feb.", "Mar.", "Apr.", "May.", "June.", "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
    mm, dd, yyyy = pk.split()
    dd = dd[:-1]

    if len(dd)<2:
        dd = "0"+dd

    date = f"{yyyy}-{months.index(mm)+1}-{dd}"

    pictures = UploadImageTest.objects.filter(date=date)
    msg = "Images posted on : "+pk
    if len(pictures)==0:
        msg = "No Image posted on "+pk

    context = {
        'object_list': pictures,
        'photos': msg
    }
    return render(request,'home.html',context)

def Uploader(request):

    if request.method == 'GET':
        form = UploadVideo() 
        context = {
            'files': Videos.objects.all(),
            'form': form
            }
    
    if request.method == 'POST':
        form = UploadVideo(request.POST,request.FILES)

        if form.is_valid():
            save_video = form.save()        
            CheckVideo(request,f"media/{Videos.objects.get(id=save_video.id).Upload_File}")
            os.remove(f"media/{Videos.objects.get(id=save_video.id).Upload_File}")
            Videos.objects.get(id=save_video.id).delete()
        
        context = {
            'message': "Completed",
            'form': form,
            }

    return render(request,'upload.html',context)

# def ObjectDetect(request,a,b,c):
#     CheckVideo(a+'/'+b+'/'+c)

#     context = {
#         'a': "Completed" #a+'/'+b+'/'+c
#     }
#     return render(request,'plastic.html',context)
