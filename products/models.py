from django.db import models
from accounts.models import User


class BaseModel(models.Model):
    # creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    created_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='category_creator')
    name = models.CharField(max_length=30, unique=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Brand(BaseModel):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='brand_creator')
    name = models.CharField(max_length=100, unique=True)


class ProductColor(BaseModel):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='color_creator')
    name = models.CharField(max_length=30)
    hex_value = models.CharField(max_length=7)


class ProductSize(BaseModel):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='size_creator')
    size = models.CharField(max_length=2)


class Product(BaseModel):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class ProductItem(BaseModel):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pro_item_creator')
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    pro_color = models.ForeignKey(ProductColor, on_delete=models.CASCADE)
    pro_size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    price = models.FloatField()


class ProductImage(BaseModel):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='image_creator')
    productitem = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    image = models.FileField(upload_to='static/productimage')










