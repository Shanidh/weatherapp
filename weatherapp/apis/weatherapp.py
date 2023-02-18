import sys
import requests
import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import authentication, permissions
from rest_framework.authentication import SessionAuthentication
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate, logout, login
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db import transaction
from weatherapp.models import CustomUser
from django.shortcuts import render, redirect
from django.http import JsonResponse

from ..services import (
    create_user,
)

from ..serializers import (CreateUserSerializer)

class LoginAPI(APIView):
    """API for Login."""

    authentication_classes = [SessionAuthentication]

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Login successful, return user data
                data = {
                   "Success": True,
                   "msg": "Login Success",
                }
                return Response(status=status.HTTP_201_CREATED, data=data)
            else:
            # Login failed
                return Response({'error': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            # Invalid data
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateAPI(APIView):
    """API for creating User"""

    authentication_classes = [SessionAuthentication]

    def post(self, request):
        try:
            serializer = CreateUserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            with transaction.atomic():
                create_user(**serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED, data=_("User created succesfully."))
        except ValidationError as e:
            mes = "\n".join(e.messages)
            raise ValidationError(mes)
        except Exception:
            error_info = "\n".join(traceback.format_exception(*sys.exc_info()))
            print(error_info)
            data = {
                "Success": False,
                "msg": "User Registration Failed",
            }
            return Response(status=status.HTTP_400_BAD_REQUEST, data=data)


class LogoutAPI(APIView):
    """API for Logout."""
    def get(self, request):
        logout(request)
        return redirect("weatherapp:login")

class WeatherAPI(APIView):
    """API for Getting Weather information of 30 cities."""  

    authentication_classes = [SessionAuthentication]

    def get(self, request):
        city_ids = [2643743,5128638,1850147,2643123,2643741,3128760,2643744,2964574,3169070,2653822,2657896,658225,524901,5391959,3451190,4164138,2644688,2968815,2988507,3128026]
        api_key = "ed027f3c0b88e63cd0475c816cd1a3b9"
        url = f"https://api.openweathermap.org/data/2.5/group?id={','.join(map(str, city_ids))}&units=metric&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            return Response(weather_data)
        else:
            data = {
                "Success": False,
                "msg": "Failed to retrieve weather data",
            }
            return Response(status=status.HTTP_400_BAD_REQUEST, data=data)
