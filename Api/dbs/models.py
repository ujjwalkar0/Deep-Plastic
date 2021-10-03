from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField
# Create your models here.

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])

class UploadImageTest(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=nameFile, blank=True, null=True)
    location = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')

class Videos(models.Model):
    Upload_File=models.FileField(upload_to='file2link')