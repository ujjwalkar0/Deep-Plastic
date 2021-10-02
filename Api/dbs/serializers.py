from rest_framework import serializers
from .models import UploadImageTest
from versatileimagefield.serializers import VersatileImageFieldSerializer


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImageTest
        fields = ('name', 'image')