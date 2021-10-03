from django import forms
from .models import Videos

class UploadVideo(forms.ModelForm):
    class Meta:
        model = Videos
        fields = [
            "Upload_File",
        ] 