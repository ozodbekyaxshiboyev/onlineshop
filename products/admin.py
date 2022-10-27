from django.contrib import admin
from .models import (
Brand,
ProductColor,
ProductSize,
Product,
ProductItem,
ProductImage
)

admin.site.register([Brand, ProductColor, ProductSize, Product, ProductItem, ProductImage])