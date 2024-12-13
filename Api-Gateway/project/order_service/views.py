from django.shortcuts import render
import requests
from rest_framework.views import APIView
from utils.services import ORDER_SERVICES_URL
from rest_framework.response import Response
# Create your views here.



class CartView(APIView):
    def post(self, request):
        service_url = f'{ORDER_SERVICES_URL}/cart/post/'
        response = requests.post(service_url,
                                 data=request.data
                                 )
        return Response(response.json(),status=response.status_code)
    def get(self,request,pk):
        service_url = f'{ORDER_SERVICES_URL}/cart/get/{pk}/'
        response = requests.get(
            service_url,
        )
        print(response.json())
        return Response(response.json(),status=response.status_code)
    
class QuantityView(APIView):
    def post(self, request):
        service_url = f'{ORDER_SERVICES_URL}/cart/quantity/'
        response = requests.post(service_url,
                                 data=request.data
                                 )
        return Response(response.json(),status=response.status_code)