from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Image,Profile, User
from .forms import EditProfile,UploadForm,CommentForm, SignUpForm


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})


@login_required(login_url='/accounts/login/')
def index(request):
    title = 'Instagrum'
    image_posts = Image.objects.all()
    return render(request, 'index.html', {"title":title,"image_posts":image_posts})

@login_required(login_url='/accounts/login/')
def profile(request, user_id):
    title = 'Instagrum |Profile'
    current_user = request.user

    # Try to get the profile or redirect if it does not exist
    profile = get_object_or_404(Profile, user__id=user_id)

    # Get user images
    photos = Image.get_user_images(user_id)

    # Check if the profile has a photo or redirect
    if not profile.profile_photo:
        return redirect('edit_profile')

    context = {
        "title": title,
        "profile": profile,
        "photos": photos, 
        "current_user": current_user,
        "user_id": user_id
    }

    return render(request,'profile.html', context)

@login_required(login_url='/accounts/login/')
def like_image(request, id):
    image = get_object_or_404(Image, id=id)
    user = request.user

    # check if the user has already liked this image
    if user in image.likers.all():
        # user has already liked this image, remove their like
        image.likers.remove(user)
        image.likes -= 1
    else:
        # user hasn't liked this image yet, add their like
        image.likers.add(user)
        image.likes += 1

    image.save()
    return redirect('index')



@login_required(login_url='/accounts/login/')
def edit_profile(request):
    title = 'Instagram |Edit'
    current_user = request.user
    
    if Profile.objects.filter(user=current_user).exists():
        profile = Profile.objects.get(user=current_user)
        if request.method == 'POST':
            form = EditProfile(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('profile', current_user.id)
            else:
                print(form.errors)
        else:
            form = EditProfile(instance=profile)
    else:
        form = EditProfile()
        profile = None

    return render(request, 'edit_profile.html', {"title": title, "form": form, "profile": profile})

@login_required(login_url='/accounts/login/')
def upload(request):
    title = 'Instagrum |Upload'
    
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = request.user
            upload.profile = request.user.profile  # Directly access the profile from request.user
            upload.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = UploadForm()

    return render(request, 'upload.html', {"title": title, "user": request.user, "form": form})

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
