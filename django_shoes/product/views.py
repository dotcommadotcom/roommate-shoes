from django.http import Http404
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSeralizers


class LatestProductList(APIView):
  def get(self, request, format=None):
    products = Product.objects.all()[0:4]
    serializer = ProductSeralizers(products, many=True)

    return Response(serializer.data)

class ProductDetail(APIView):
  def get_object(self, _category_slug, _product_slug):
    try:
      return Product.objects.filter(category__slug=_category_slug).get(slug=_product_slug)
    except Product.DoesNotExist:
      raise Http404

  def get(self, request, _category_slug, _product_slug, format=None):
    product = self.get_object(_category_slug, _product_slug)
    serializer = ProductSeralizers(product, many=True)

    return Response(serializer.data)
