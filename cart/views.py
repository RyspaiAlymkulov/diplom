from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Cart, DeliveryCost
from .serializers import UserCartSerializer, CartSerializer, DeliveryCostSerializer
from django.contrib.auth.models import User


class UserListAPIview(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserCartSerializer


class CartListAPIview(generics.ListCreateAPIView):
    queryset = Cart.objects.all().order_by('id')
    serializer_class = CartSerializer


class DeliveryListAPIview(generics.ListCreateAPIView):
    queryset = DeliveryCost.objects.all().order_by('id')
    serializer_class = DeliveryCostSerializer