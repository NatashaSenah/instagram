from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Image
# from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def welcome(request):
    images=Image.objects.all()
    print(images)
    return render(request,'all-instagram/instagram.html',{"images":images})

@login_required
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_by_image_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-instagram/search.html',{"message":message,"image": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-instagram/search.html',{"message":message})

# @login_required(login_url='/accounts/login/')
# def new_user(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = NewUserForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.editor = current_user
#             user.save()
#         return redirect('Instagram')

#     else:
#         form = NewUserForm()
#     return render(request, 'new_user.html', {"form": form})
# def image(request,image_id):
#     # try:
#     #     image = Image.objects.get(id = image_id)
#     # except DoesNotExist:
#     #     raise Http404()
#     # return render(request,"all-instagram/instagram.html", {"image":image})
#     if request.method == 'POST':
#         form = NewsLetterForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['your_name']
#             email = form.cleaned_data['email']
#             recipient = NewsLetterRecipients(name = name,email =email)
#             recipient.save()
#             send_welcome_email(name,email)
#             HttpResponseRedirect('image')
#     else:
#         form = NewsLetterForm()
#     return render(request, 'all-instagram/instagram.html', {"date": date,"instagrams":instagrams,"letterForm":form})