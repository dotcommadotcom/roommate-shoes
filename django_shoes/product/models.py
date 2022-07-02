from unicodedata import category, name
from django.db import models

class Category(models.Model):
  name = models.CharField(max=255)
  slug = models.SlugField()

  class Meta:
    ordering = ('name', )

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return f'/{self.slug}/'

# class Product(models.Model):
#   category = Category.
#   name = models.CharField(max=255)
#   slug = models.SlugField()

#   class Meta:
#     ordering = ('-date_added', )

#   def __str__(self):
#     return self.name

#   def get_absolute_url(self):
#     return f'/{self.category}/{self.slug}/'

