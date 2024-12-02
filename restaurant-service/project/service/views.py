from decimal import Decimal
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, Menu, Restaurant
from .serializers import CategorySerializer, MenuPostSerializer, MenuSerializer, RestaurantSerializer
from rest_framework import status
# Create your views here.


class RestaurantView(APIView):
    def post(self,request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            rest = Restaurant.objects.filter(user_id=serializer.validated_data['user_id'])
            print(rest)
            if rest:
                return Response({'msg':'why the fuck are you trying to add next Restaurant!!!'},status=status.HTTP_208_ALREADY_REPORTED)
            Restaurant.objects.create(
                user_id = serializer.validated_data['user_id'],
                name = serializer.validated_data['name'],
                license_image = serializer.validated_data['license_image'],
                latitude = Decimal(serializer.validated_data['latitude']),
                longitude = Decimal(serializer.validated_data['longitude']),
                open_time = serializer.validated_data['open_time'],
                close_time = serializer.validated_data['close_time']
            )
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class CategoryView(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        cat = Category.objects.all()
        serializer = CategorySerializer(cat,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class MenuView(APIView):
    def post(self, request):
        try:
            restaurant = Restaurant.objects.get(user_id=request.data['user_id'])
        except Restaurant.DoesNotExist:
            return Response({'err':'Restaurant Does Not Exist!'},status=status.HTTP_404_NOT_FOUND)
        data = request.data.copy()
        print(restaurant.id)
        data['restaurant'] = restaurant.id
        serializer = MenuPostSerializer(data=data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk=None):
        if pk:
            try:
                restaurant = Restaurant.objects.get(user_id=pk)
            except Restaurant.DoesNotExist:
                return Response({'err':'Restaurant Does Not Exist!'},status=status.HTTP_404_NOT_FOUND)
            menu = Menu.objects.filter(restaurant = restaurant)
        else:
            menu = Menu.objects.all()
        serializer = MenuSerializer(menu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
