from django import forms
from .models import Image,Profile

class UploadForm(forms.ModelForm):
      class Meta:
            model = Image
            exclude = ['user','profile','likes']

class EditProfile(forms.ModelForm):
      class Meta:
            model = Profile
            exclude = ['user']