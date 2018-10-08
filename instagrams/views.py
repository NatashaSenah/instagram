from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Image,Profile
from django.contrib.auth.models import User
from .forms import ProfileForm,ImageForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def welcome(request):
    images=Image.objects.all()
    print(images)
    return render(request,'all-instagram/instagram.html',{"images":images})

# @login_required
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_by_image_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-instagram/search.html',{"message":message,"image": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-instagram/search.html',{"message":message})
# @login_required(login_url='/login')

def profile(request, username):
    profile = User.objects.get(username=username)
 
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    images = Image.get_profile_images(profile.id)
    title = f'@{profile.username} Instagram photos and videos'

    return render(request, 'profile/profile.html', {'title':title, 'profile':profile, 'profile_details':profile_details, 'images':images})
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('edit_profile')
    else:
        form = ProfileForm()

    return render(request, 'profile/edit_profile.html', {'form': form})
@login_required(login_url='/accounts/login')
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.profile = request.user
            # print(f'image is {upload.image}')
            upload.save()
            return redirect('profile', username=request.user)
    else:
        form = ImageForm()
    
    return render(request, 'profile/upload_image.html', {'form':form})