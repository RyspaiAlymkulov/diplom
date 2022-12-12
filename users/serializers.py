from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserAbstractSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserLoginSerializer(UserAbstractSerializer):
    pass


class UserRegisterSerializer(UserAbstractSerializer):

    def validate_username(self, username):
        if User.objects.filter(username=username):
            raise ValidationError('Пользователь с таким профилем уже существует')
        return username