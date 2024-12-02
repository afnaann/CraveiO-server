import requests
from rest_framework.views import APIView
from utils.services import USER_SERVICES_URL
from rest_framework.response import Response


class SignupView(APIView):
    def post(self,request):
        service_url = f'{USER_SERVICES_URL}/user/signup/'
        response = requests.post(service_url,data=request.data)
        return Response(response.json(),status=response.status_code)
    
class LoginView(APIView):
    def post(self,request):
        service_url = f'{USER_SERVICES_URL}/user/signin/'
        response = requests.post(service_url,data=request.data)
        return Response(response.json(),status=response.status_code)

class GoogleAuthView(APIView):
    def post(self,request):
        service_url = f'{USER_SERVICES_URL}/user/google/'
        response = requests.post(service_url,data=request.data)
        return Response(response.json(),status=response.status_code)
