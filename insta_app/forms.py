from django import forms
from .models import Image,Profile,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UploadForm(forms.ModelForm):
      class Meta:
            model = Image
            exclude = ['user','profile','likes', 'likers']

class EditProfile(forms.ModelForm):
      class Meta:
            model = Profile
            exclude = ['user']

class CommentForm(forms.ModelForm):
      class Meta:
            model = Comment
            fields = ['comments',]


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
            ]