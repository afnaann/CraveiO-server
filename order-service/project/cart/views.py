from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .serializer import CartSerializer
from .models import Cart, CartItem
from rest_framework import status


RESTAURANT_SERVICES_URL = 'http://127.0.0.1:8500/restaurant/products/'

class CartView(APIView):
    def post(self, request):
        data = request.data
        try:
            cart = Cart.objects.get(user_id=data['user_id'])
        except Cart.DoesNotExist:
            return Response({'msg':'This User Is Not Allowed To Use Cart'},status=status.HTTP_401_UNAUTHORIZED)
        cartItem, created = CartItem.objects.get_or_create(cart=cart,product_id=data['dish_id'])
        if created:
            cartItem.quantity = 1
        else:
            cartItem.quantity += 1
        cartItem.save()
        return Response({'msg':'creation Success!'},status=status.HTTP_201_CREATED)
    
    
    def get(self, request, pk):
        try:
            cart = Cart.objects.get(user_id=pk)
        except Cart.DoesNotExist:
            return Response({'msg': 'This User Is Not Allowed To Use Cart'}, status=status.HTTP_401_UNAUTHORIZED)

        items = cart.cartitem_set.all()

        product_ids = [item.product_id for item in items]

        if not product_ids:
            return Response({'cart': []}, status=status.HTTP_200_OK)

        try:
            response = requests.get(RESTAURANT_SERVICES_URL, params={'ids': ','.join(map(str, product_ids))})
            response.raise_for_status()  # Raise an exception for HTTP errors
            product_data = {str(p['id']): p for p in response.json().get('products', [])}
        except requests.RequestException as e:
            return Response({'error': 'Failed to fetch product details', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        cart_response = []
        for item in items:
            product_detail = product_data.get(str(item.product_id), {})
            cart_response.append({
                'product_id': item.product_id,
                'quantity': item.quantity,
                'product_details': product_detail
            })
        # print(cart_response.values())
        return Response({'cart': cart_response}, status=status.HTTP_200_OK)
    
    

class QuantityView(APIView):
    def post(self, request):
        data = request.data
        try:
            cart = Cart.objects.get(user_id=data['user_id'])
        except Cart.DoesNotExist:
            return Response({'msg':'This User Does Not Have Cart'},status=status.HTTP_401_UNAUTHORIZED)
        print(cart)
        try:
            cartitem = CartItem.objects.get(cart=cart,product_id=data['product_id'])
        except Cart.DoesNotExist:
            return Response({'msg':'This User Does Not Have Cart Item'},status=status.HTTP_401_UNAUTHORIZED)
        print(cartitem)
        print(data['newQuantity'])
        if data['newQuantity'] == '0':
            cartitem.delete()
        else:
            cartitem.quantity = data['newQuantity']
            cartitem.save()
        print(cartitem.quantity)
        return Response({'msg':'Cart Updated Successfully!'},status=status.HTTP_200_OK)