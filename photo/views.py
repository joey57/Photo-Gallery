from django.shortcuts import render
from django.http  import HttpResponse, Http404
from .models import Image, Category, Location

# Create your views here.

def index(request):
    images = Image.get_all_images()

    return render(request, 'index.html', {'images':images})
