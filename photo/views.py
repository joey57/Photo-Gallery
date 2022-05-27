from django.shortcuts import render
from django.http  import HttpResponse, Http404
from .models import Image, Category, Location

# Create your views here.

def index(request):
    images = Image.get_all_images()
    locations = Location.objects.all()

    return render(request, 'index.html', {'images':images, 'images':images, 'locations':locations })

def search_image(request):
    title = 'Search'
    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'image_category' in request.GET and request.GET['image_category']:
        search_term = request.GET.get('image_category')
        found_results = Image.search_by_category(search_term)
        message = f"{search_term}"
        print(search_term)
        print(found_results)

        return render(request, 'search.html', {'title':title,'images': found_results, 'message': message, 'categories': categories, 'locations':locations})
        




