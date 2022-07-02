from rest_framework import serializers

from .models import Category, Product

class ProductSeralizers(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = [
      "id",
      "name",
      "get_absolute_url",
      "description",
      "price",
      "get_image_url",
      "get_thumbnail_url",
    ]
