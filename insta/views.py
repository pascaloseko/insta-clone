from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404
from .models import Image,Profile,Comment
from .forms import EditProfile,UploadForm,CommentForm

# Create your views here.
def index(request):
    title = 'Instagrum'
    image_posts = Image.objects.all()
    return render(request, 'index.html', {"title":title,"image_posts":image_posts})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    title = 'Instagrum |Profile'
    profiles = Profile.objects.all()
    return render(request,'profile.html',{"title":title,"profiles":profiles,"user":current_user,})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    title = 'Instagram |Edit'
    current_user = request.user
    if request.method == 'POST':
        form = EditProfile(request.POST,request.FILES)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = current_user
            update.profile = current_profile
            update.save()
            return redirect('profile')
    else:
        form = EditProfile()
    return render(request, 'edit_profile.html', {"title":title, "form":form})

@login_required(login_url='/accounts/login/')
def upload(request):
    title = 'Instagrum |Upload'
    current_user = request.user         
    profiles = Profile.get_profile()
    for profile in profiles:
        if profile.user.id == current_user.id:
            if request.method == 'POST':
                form = UploadForm(request.POST,request.FILES)
                if form.is_valid():
                    upload = form.save(commit=False)
                    upload.user = current_user
                    upload.profile = profile
                    upload.save()
                    return redirect('index')
            else:
                form = UploadForm()
        return render(request,'upload.html',{"title":title, "user":current_user,"form":form})

@login_required(login_url='/accounts/login/')
def post_comment(request, id):
    title = 'Instagrum |Comment'
    post = get_object_or_404(Image, id=id)
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post_comment = form.save(commit=False)
            post_comment.user = current_user
            post_comment.pic = post
            post_comment.save()
            return redirect('index')
    else:
        form = CommentForm()
        
    return render(request,'comments.html',{"title":title,"form":form})

def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})