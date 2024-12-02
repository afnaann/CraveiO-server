from rest_framework import serializers

from .models import Category, Restaurant,Menu

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['user_id','name','license_image','latitude','longitude','open_time','close_time']
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','id']
        

class MenuSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()
    class Meta:
        model = Menu
        fields = ['restaurant','dish_image','name','description','price','category']

class MenuPostSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    class Meta:
        model = Menu
        fields = ['restaurant','dish_image','name','description','price','category']
