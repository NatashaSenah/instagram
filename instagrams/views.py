from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image
# Create your views here.
def welcome(request):
    return render(request,'welcome.html',{'name':'instagram'})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_by_image_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-instagram/search.html',{"message":message,"image": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-instagram/search.html',{"message":message})


def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-instagram/instagram.html", {"image":image})