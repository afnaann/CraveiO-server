from rest_framework import serializers

from .models import Cart, CartItem

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product_id','quantity']