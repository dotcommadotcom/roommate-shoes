from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSeralizers


class LatestProductList(APIView):
  def get(self, request, format=None):
    serializer = ProductSeralizers(Product.objects.all()[0:4], many=True)

    return Response(serializer.data)
