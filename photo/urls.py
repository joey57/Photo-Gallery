from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  path('', views.index , name = 'index'),
  path('search/', views.search_image, name = 'search_image'),
  re_path('location/(?P<image_location>\d+)', views.location_filter, name = 'location_filter'),
  re_path('image/(<category_name>)/(<image_id>\d+)', views.single, name = 'single'),
]
if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)