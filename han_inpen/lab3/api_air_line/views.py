from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (
    CustomTokenObtainPairSerializer, user_token,User_serializer,Airline_serializer,Passenger_serializer,Review_serializer,Air_travel_serializer
)
from django.contrib.auth.models import User



class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(
            username=username,
            password=password
        )
        if user:
            login_serializer = self.serializer_class(data=request.data)
            if user.is_active:
                if login_serializer.is_valid():
                    user_serializer = user_token(user)
                    
                    return Response({
                        'token': login_serializer.validated_data.get('access'),
                        'refresh-token': login_serializer.validated_data.get('refresh'),
                        'user': user_serializer.data,
                        'message': 'Successful Login'
                    }, status=status.HTTP_200_OK)
                return Response({'error': 'wrong username or password'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'error': 'user not active'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'wrong username or password'}, status=status.HTTP_400_BAD_REQUEST)

class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user', 0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'logged out successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'user does not exist'}, status=status.HTTP_400_BAD_REQUEST)

class Airline_viewsets (viewsets.ModelViewSet):
    serializer_class = Airline_serializer
    permission_classes = (IsAuthenticated,)
    queryset = Airline_serializer.Meta.model.objects.all()   

class Passenger_viewsets (viewsets.ModelViewSet):
    serializer_class = Passenger_serializer
    permission_classes = (IsAuthenticated,)
    queryset = Passenger_serializer.Meta.model.objects.all()  

class Review_viewsets (viewsets.ModelViewSet):
    serializer_class = Review_serializer
    permission_classes = (IsAuthenticated,)
    queryset = Review_serializer.Meta.model.objects.all()  

class User_viewsets (viewsets.ModelViewSet):
    serializer_class = User_serializer
    permission_classes = (IsAuthenticated,)
    queryset = User_serializer.Meta.model.objects.all()  

class Air_travel_viewsets (viewsets.ModelViewSet):
    serializer_class = Air_travel_serializer
    permission_classes = (IsAuthenticated,)
    queryset = Air_travel_serializer.Meta.model.objects.all()  