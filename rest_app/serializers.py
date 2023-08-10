from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import MultipleChoiceField, Field
from rest_framework.serializers import ModelSerializer

from rest_app.models import Product, Category


class ProductSerializer(ModelSerializer):

    discount = serializers.ChoiceField(choices=[0, 10, 15, 20, 30, 50])

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'discount', 'end_price', 'category', 'description']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
