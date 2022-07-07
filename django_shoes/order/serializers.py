from rest_framework import serializers

from django_shoes.product.serializers import ProductSeralizer

from .models import Order, OrderItem

class UserOrderItemSerializer(serializers.ModelSerializer):
  product = ProductSeralizer()

  class Meta:
    model = OrderItem
    fields = [
      "price",
      "product",
      "quantity"
    ]

class UserOrderSerializer(serializers.ModelSerializer):
  items = UserOrderItemSerializer(many=True)

  class Meta:
    model = Order
    fields = [
      "id",
      "first_name",
      "last_name",
      "email",
      "items",
      "paid_amount",
    ]

class OrderItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = OrderItem
    fields = [
      "price",
      "product",
      "quantity"
    ]

class OrderSerializer(serializers.ModelSerializer):
  items = OrderItemSerializer(many=True)

  class Meta:
    model = Order
    fields = [
      "id",
      "first_name",
      "last_name",
      "email",
      "items",
    ]

  def create(self, validated_data):
    items_data = validated_data.pop('items')
    order = Order.objects.create(**validated_data)

    for item_data in items_data:
      OrderItem.objects.create(order=order, **item_data)

    return order
