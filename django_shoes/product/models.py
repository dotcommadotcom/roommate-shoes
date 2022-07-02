from PIL import Image
from io import BytesIO

from django.core.files import File
from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=255)
  slug = models.SlugField()

  class Meta:
    ordering = ('name', )

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return f'/{self.slug}/'

class Product(models.Model):
  category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  slug = models.SlugField()
  description = models.TextField(blank=True, null=True)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  image = models.ImageField(upload_to='uploads/', blank=True, null=True)
  thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('-date_added', )

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return f'/{self.category.slug}/{self.slug}/'

  def get_image_url(self):
    return 'http://127.0.0.1:8000' + self.image.url if self.image else ''

  def make_thumbnail(self, image, size=(600, 400)):
    img = Image.open(image)
    img.convert('RGB')
    img.thumbnail(size)

    thumb_io = BytesIO()
    img.save(thumb_io, 'JPEG', quality=85)

    return File(thumb_io, name=image.name)

  def get_thumbnail_url(self):
    if not self.image:
      return ''

    if not self.thumbnail:
      self.thumbnail = self.make_thumbnail(self.image)
      self.save()

    return 'http://127.0.0.1:8000' + self.thumbnail.url
    

