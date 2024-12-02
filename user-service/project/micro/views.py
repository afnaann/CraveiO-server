from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from google.oauth2 import id_token
from google.auth.transport import requests
from django.conf import settings

from .customToken import CustomToken

from .models import CustomUser, Roles
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class SignupView(APIView):
    def post(self,request):
        print('request:',request.data)
        if request.data['password'] != request.data['confirmPassword']:
            return Response({'msg':'password Does Not Match'},status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print('serialied data: ',serializer.data)
            user = CustomUser.objects.create_user(name=serializer.data['name'],email=serializer.data['email'],password=serializer.data['password'])
            print('user: ',user)
            return Response({'msg':'user Created Successfully!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class GoogleLoginView(APIView):
    def post(self, request):
        token = request.data.get("token")
        try:
            id_info = id_token.verify_oauth2_token(token, requests.Request(), settings.GOOGLE_CLIENT_ID)
            email = id_info.get("email")
            name = id_info.get("name")

            if not email:
                return Response({"error": "Email not available in Google account"}, status=status.HTTP_400_BAD_REQUEST)

            user, created = CustomUser.objects.get_or_create(
                email=email,
                defaults={
                    "name": name,
                    "role": "CUSTOMER",  
                }
            )

            refresh = CustomToken(user)

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "is_new_user": created,
            })

        except ValueError as e:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)


class UserStatusView(APIView):
    def patch(self,request):
        if request.data['role'] in Roles:
            user = CustomUser.objects.get(id=request.data['user_id'])
            user.role = Roles[request.data['role']]
            user.save()
            return Response({'hai':'yes'},status=status.HTTP_200_OK)
        return Response({'hai':'no'},status=status.HTTP_400_BAD_REQUEST)