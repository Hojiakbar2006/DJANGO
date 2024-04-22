from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator, ValidationError
from rest_framework import serializers
from django.core.exceptions import ValidationError

from .models import CustomUser
from rest_framework.validators import UniqueValidator



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name',
                  'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


def validate_username(value):
    if not value.isalnum():
        raise ValidationError(
            'Foydalanuvchi nomi faqat harflar, raqamlar va _ belgisidan iborat bo\'lishi kerak.'
        )


def validate_email(value):
    if CustomUser.objects.filter(email=value).exists():
        raise ValidationError('Bu e-mail allaqachon ro\'yxatdan o\'tgan')


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=50,
        validators=[
            UniqueValidator(
                queryset=CustomUser.objects.all(), message='Bu foydalanuvchi nomi mavjud'),
            validate_username,
        ]
    )
    email = serializers.EmailField(validators=[validate_email])
    password = serializers.CharField(
        max_length=128,
        write_only=True,
    )

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError(
                'Parol kamida 6 ta belgidan iborat bo\'lishi kerak.')
        return value

    def validate(self, data):
        if not data.get('username'):
            raise serializers.ValidationError(
                {'username': 'Foydalanuvchi nomi maydoni bo\'sh bo\'lmasligi kerak.'})

        if not data.get('email'):
            raise serializers.ValidationError(
                {'email': 'E-mail maydoni bo\'sh bo\'lmasligi kerak.'})

        if not data.get('password'):
            raise serializers.ValidationError(
                {'password': 'Parol maydoni bo\'sh bo\'lmasligi kerak.'})

        return data
