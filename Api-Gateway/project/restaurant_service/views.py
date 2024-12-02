from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.services import RESTAURANT_SERVICES_URL,USER_SERVICES_URL
# Create your views here.

class RestaurantView(APIView):
    def post(self, request):
    
        files = {}
        if 'license_image' in request.data:
            files['license_image'] = request.data.get('license_image')
            request.data.pop('license_image')
            
        response = requests.post(f'{RESTAURANT_SERVICES_URL}/restaurant/join/',
                                 files=files,
                                 data=request.data,
                                 headers={key: value for key, value in request.headers.items() if key != 'Content-Type'}
                                 
                                 )
        if response.status_code == 201:
            user_role = {
                'user_id':request.data['user_id'],
                'role':'SHOP_OWNER'
            }
            res = requests.patch(f'{USER_SERVICES_URL}/user/status/',data=user_role)
            print(res)
        return Response(response.json(),status=response.status_code)
    
class CategoryView(APIView):
    def post(self,request):
        service_url = f'{RESTAURANT_SERVICES_URL}/restaurant/category/'
        response = requests.post(service_url,
                                 data=request.data
                                 )
        return Response(response.json(),status=response.status_code)
    def get(self,request):
        service_url = f'{RESTAURANT_SERVICES_URL}/restaurant/category/'
        response = requests.get(
            service_url,
        )
        return Response(response.json(),status=response.status_code)

class MenuView(APIView):
    def post(self, request):
        print(request.data)
        files = {}
        if 'dish_image' in request.data:
            files['dish_image'] = request.data.get('dish_image')
            request.data.pop('dish_image')
        response = requests.post(f'{RESTAURANT_SERVICES_URL}/restaurant/menu/',
                                 files=files,
                                 data=request.data,
                                 headers={key: value for key, value in request.headers.items() if key != 'Content-Type'}
                                 )
        print(response)
        return Response(response.json(),status=response.status_code)
    def get(self,request,pk=None):
        if pk:
            service_url = f'{RESTAURANT_SERVICES_URL}/restaurant/menu/{pk}/'
        else:   
            service_url = f'{RESTAURANT_SERVICES_URL}/restaurant/menu/'
        response = requests.get(
            service_url,
            data=request.data
        )
        
        return Response(response.json(),status=response.status_code)
