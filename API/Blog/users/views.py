# myproject/users/views.py

from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import CustomUserSerializer, SignupSerializer


from rest_framework_simplejwt.tokens import RefreshToken


class SignupView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            # Foydalanuvchi ro'yxatdan o'tadi
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = CustomUser.objects.create_user(
                username=username, email=email, password=password)

            # Token generatsiya qilish
            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            return Response({'message': 'Ro\'yxatdan o\'tish muvaffaqiyatli', 'token': token, }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)


                return Response(
                    {
                        'message': 'Kirish muvaffaqiyatli',
                        'success': True,
                        'access_token': access_token,
                        # 'refresh_token':refresh
                    }, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Foydalanuvchi faol emas', 'success': False}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Login yoki parol xato', 'success': False}, status=status.HTTP_400_BAD_REQUEST)


class TokenRefreshExtendedView(TokenRefreshView):
    pass


class UpdateUserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        user.save()

        new_password = data.get('password')
        if new_password:
            user.set_password(new_password)
            user.save()

        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
