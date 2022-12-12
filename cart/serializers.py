from .models import Cart, DeliveryCost
from rest_framework import serializers
from django.contrib.auth.models import User


class UserCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'created_at', 'updated_at']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'item_caps', 'quantity_caps', 'created_at', 'updated_at']


class DeliveryCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCost
        fields = ['id', 'status', 'cost_of_delivery_caps', 'cost_of_caps', 'fixed_price', 'created_at', 'updated_at']