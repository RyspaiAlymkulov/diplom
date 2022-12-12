# from users.serializers import ProfileSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from users.serializers import UserLoginSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from users.serializers import UserRegisterSerializer
from rest_framework import status

from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from django.contrib.auth.models import User


class RegisterAPIview(APIView):
    def register(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(
            username=serializer.validated_data.get('username'),
            password=serializer.validated_data.get('password')
        )
        return Response(status=status.HTTP_201_CREATED)


class LoginAPIview(APIView):
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            return Response(status=status.HTTP_403_FORBIDDEN,
                            data={'message': 'User data are wrong'})
        else:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(data={'key': token.key})
