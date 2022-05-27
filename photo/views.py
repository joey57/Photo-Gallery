from unicodedata import category
from django.shortcuts import render
from django.http  import HttpResponse, Http404
from .models import Image, Category, Location

# Create your views here.

def index(request):
    images = Image.get_all_images()
    locations = Location.objects.all()

    return render(request, 'index.html', {'images':images, 'locations':locations })    

def search_image(request):
    title = 'Search'
    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'image_category' in request.GET and request.GET['image_category']:
        search_term = request.GET.get('image_category')
        found_results = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {'title':title,'images': found_results, 'message': message, 'categories': categories, 'locations':locations})
    else:
        message = 'You havent searched yet'
        return render(request, 'search.html',{"message": message})    

def location_filter(request, image_location):
    locations = Location.objects.all()
    location = Location.get_location_id(image_location)
    images = Image.filter_by_location(image_location)
    title = f'{location} Photos'
    return render(request, 'location.html', {'title':title, 'images':images, 'locations':locations, 'location':location})

def single(request,image_id, category_name):
    title = 'Image'
    locations =Location.objects.all()
    image_category = Image.objects.filter(image_category__name = category_name)
    try:
        image = Image.objects.get(id = image_id)
    except:
        raise Http404()
    return render(request,"single.html",{"title":title, "image":image, "locations":locations, "image_category":image_category})





