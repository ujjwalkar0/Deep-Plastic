from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField

class UploadImageTest(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Images/", blank=True, null=True)
    location = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Videos(models.Model):
    Upload_File=models.FileField(upload_to='file2link/')