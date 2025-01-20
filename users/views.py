from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from drf_spectacular.utils import extend_schema, extend_schema_view
from .serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    TokenResponseSerializer,
    UserCreatedResponseSerializer,
)

from django.contrib.auth import get_user_model

User = get_user_model()

@extend_schema_view(
    post=extend_schema(
        request=UserRegisterSerializer,
        responses={
            201: UserCreatedResponseSerializer,
            400: {"description": "Invalid data"}
        },
    )
)
class UserRegisterView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        if User.objects.filter(email=email).exists():
            raise ValidationError("User with this email already exists.")
        
        User.objects.create_user(email=email, password=password)
        return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)


@extend_schema_view(
    post=extend_schema(
        request=UserLoginSerializer,
        responses={
            200: TokenResponseSerializer,
            401: {"description": "Invalid credentials"},
            400: {"description": "Invalid data"}
        },
    )
)
class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(request, email=email, password=password)
        if user is None:
            return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_200_OK)
