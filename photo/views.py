from django.shortcuts import render
from django.http  import HttpResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    title = 'Gallery'

    return render(request, 'index.html', {'title':title})
