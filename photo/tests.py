from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.
class ImageTestClass(TestCase):
  #setUp method
  def setUp(self):
    self.cat = Category(name = 'Fashion')
    self.cat.save_category()

    self.loc = Location(name = 'Africa')
    self.loc.save_location()

    self.image = Image(name = 'test', description = 'desc test', image_location = self.loc, image_category = self.cat)
    self.image.save_image()

  def test_instance(self):
    self.assertTrue(isinstance(self.image, Image))  


class LocationTestClass(TestCase):
  #setUp method
  def setUp(self):
    self.loc = Location(name = 'Africa')
    self.loc.save_location()

  def test_instance(self):
    self.assertTrue(isinstance(self.loc, Location))  

class CategoryTestClass(TestCase):
  # set up method 
  def setUp(self):
    self.cat = Category(name = 'Fashion')
    self.cat.save_category()

  def test_instance(self):
    self.assertTrue(isinstance(self.cat, Category))



