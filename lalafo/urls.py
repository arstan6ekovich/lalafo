from django.urls import path
from .views import (
    CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,
)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/add/', CategoryCreateView.as_view(), name='category_add'),
    path('category/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_edit'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    path('products/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
