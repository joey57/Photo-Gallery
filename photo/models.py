from django.db import models
from django.forms import ImageField

# Create your models here.
class Image(models.Model):
  name = models.CharField(max_length=50)
  pic = models.ImageField(upload_to = 'uploads/')
  description = models.TextField()
  image_location = models.ForeignKey('Location',on_delete=models.CASCADE)
  image_category = models.ForeignKey('Category',on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class Location(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name  
