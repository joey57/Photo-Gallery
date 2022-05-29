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
    print(images)
    self.assertTrue(len(images) > 0)

  def test_search_by_category(self):
    images = Image.search_by_category('Fashion')
    self.assertTrue(len(images)> 0)

  def test_update_image(self):
    image = Image.update_image(self.image.id, 'test update', 'my test', self.loc, self.cat)
    upimage = Image.objects.filter(id = self.image.id)
    print(upimage)
    self.assertTrue(Image.name == 'test update')     


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



