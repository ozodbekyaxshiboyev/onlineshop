from django.db import models
from products.models import BaseModel, ProductItem
from accounts.models import User


class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    text = models.TextField()


class Rating(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(blank=True, null=True)


class Wishlist(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
