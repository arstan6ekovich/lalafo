from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Category (models.Model):
    category_photo = models.ImageField(upload_to='category_photo/')
    category_name = models.CharField(max_length=34, unique=True)

    def __str__(self):
        return self.category_name

class Product (models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=64)
    product_image = models.ImageField(upload_to='product_image/')
    product_price = models.PositiveSmallIntegerField()
    product_phone_number = PhoneNumberField()
    product_description = models.TextField()
    product_type = models.BooleanField()

    def __str__(self):
        return f'{self.category}, {self.product_name}'