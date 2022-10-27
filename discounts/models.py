from django.db import models

from accounts.models import User
from products.models import BaseModel, ProductItem
from .enums import DiscountTypes


class Discount(BaseModel):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dis_creator")
    type = models.CharField(max_length=20, choices=DiscountTypes.choices(), blank=True, null=True)
    percentage = models.FloatField()
    amount = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()


class DiscountItem(BaseModel):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dis_item_creator")
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    buy_count = models.PositiveIntegerField()
    discount_count = models.PositiveIntegerField()
