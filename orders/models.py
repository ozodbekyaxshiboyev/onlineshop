from django.db import models
from accounts.models import User
from products.models import BaseModel, ProductItem



class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=6)


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_item = models.ForeignKey(ProductItem,on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
