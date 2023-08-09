from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from rest_app.models import Product, Category


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'discount', 'category', 'description']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
