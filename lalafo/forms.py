from django import forms
from .models import Category, Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'category_photo']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'category',
            'product_name',
            'product_image',
            'product_price',
            'product_phone_number',
            'product_description',
            'product_type',
        ]
