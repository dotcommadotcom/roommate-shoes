from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, OrderItem
from .serializers import OrderSerializer

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
  serializer = OrderSerializer(data=request.data)

  if serializer.is_valid():
    _paid_amount = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])
    serializer.save(user=request.user, paid_amount=_paid_amount)

    return Response(serializer.data, status=status.HTTP_201_CREATED)

  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  