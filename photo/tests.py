from unicodedata import category
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

  def tearDown(self):
    self.image.delete_image()
    self.cat.delete_category()
    self.loc.delete_location()   

  def test_save_method(self):
    self.image.save_image() 
    images = Image.objects.all() 
    self.assertTrue(len(images)> 0) 
  
  def test_get_image_by_id(self):
    images = Image.get_image_by_id(self.image.id)
    self.assertTrue(len(images) == 1)
   

  def test_filter_by_location(self):
    images = Image.filter_by_location('1') 
    self.assertTrue(len(images) > 0)

  def test_search_by_category(self):
    images = Image.search_by_category('Fashion')
    self.assertTrue(len(images)> 0)
      

class LocationTestClass(TestCase):
  #setUp method
  def setUp(self):
    self.loc = Location(name = 'Africa')
    self.loc.save_location()

  def test_instance(self):
    self.assertTrue(isinstance(self.loc, Location))  

  def test_save_method(self):
    self.loc.save_location()
    locations = Location.objects.all()
    self.assertTrue(len(locations) > 0)

  def test_delete_method(self):
    self.loc.save_location()
    self.loc.delete_location() 
    location = Location.objects.all() 
    self.assertTrue(len(location) == 0)

  def test_update(self):
    location = Location.get_location_id(self.loc.id)
    location.update_location('Donholm')
    location = Location.get_location_id(self.loc.id)
    self.assertTrue(location.name == 'Donholm')

class CategoryTestClass(TestCase):
  # set up method 
  def setUp(self):
    self.cat = Category(name = 'Fashion')
    self.cat.save_category()

  def test_instance(self):
    self.assertTrue(isinstance(self.cat, Category))

  def test_save_method(self):
    self.cat.save_category() 
    category = Category.objects.all()
    self.assertTrue(len(category) > 0)

  def test_delete_method(self):
    self.cat.save_category()
    self.cat.delete_category()
    category = Category.objects.all() 
    self.assertTrue(len(category) == 0)

  def test_update(self):
    category = Category.get_category_id(self.cat.id)
    category.update_category('Travel')
    category = Category.get_category_id(self.cat.id)
    self.assertTrue(category.name == 'Travel')




