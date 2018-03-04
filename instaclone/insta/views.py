from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Image,Profile

# Create your views here.
def index(request):
      title = 'Instagrum'
      image_posts = Image.objects.all()
      return render(request, 'index.html', {"title":title,"image_posts":image_posts})


@login_required(login_url='/accounts/login/')
def profile(request):
    title = 'Instagrum | Profile'
    profiles = Profile.objects.all()
    return render(request,'profile.html',{"title":title,"profiles":profiles})

@login_required(login_url='/accounts/login/')
def upload(request):
    title = 'Instagrum | Upload'
    return render(request,'upload.html',{"title":title})