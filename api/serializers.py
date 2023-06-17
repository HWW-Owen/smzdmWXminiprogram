from rest_framework import serializers
from .models import Product,UserProduct
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class UserProductSerializer(serializers.ModelSerializer):
    product=ProductSerializer()
    class Meta:
        model=UserProduct
        fields="__all__"
