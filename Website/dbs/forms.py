from django import forms
from .models import Videos
from django.contrib.auth.forms import AuthenticationForm

class UploadVideo(forms.ModelForm):
    class Meta:
        model = Videos
        fields = [
            "Upload_File",
        ] 
    def __init__(self, *args, **kwargs):
        super(UploadVideo, self).__init__( *args, **kwargs)

        for i in self.fields:
            self.fields[i].label = False
            self.fields[i].widget.attrs['class'] = 'form-control'


class LoginForm(AuthenticationForm):    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__( *args, **kwargs)

        for i in self.fields:
            self.fields[i].label = False
            self.fields[i].widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'