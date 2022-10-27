from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import mixins, status

from .models import (
Category,
Brand,
ProductColor,
ProductSize,
Product,
ProductItem,
ProductImage,
)
from .serializers import (
CategorySerializer,
BrandSerializer,
ProductColorSerializer,
ProductSizeSerializer,
ProductSerializer,
ProductItemSerializer,
ProductImageSerializer,
)


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer