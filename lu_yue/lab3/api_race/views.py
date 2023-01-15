from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (
    CustomTokenObtainPairSerializer, user_token,Team_serializer,Race_serializer, Comment_serializer, Rider_serializer,Comment_serializer
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

class Team_viewsets (viewsets.ModelViewSet):
    serializer_class = Team_serializer
    permission_classes = (IsAuthenticated,)
    queryset = Team_serializer.Meta.model.objects.all()   

class Race_viewsets (viewsets.ModelViewSet):
    serializer_class = Race_serializer
    permission_classes = (IsAuthenticated,)
    queryset = Race_serializer.Meta.model.objects.all()  

class Rider_viewsets (viewsets.ModelViewSet):
    serializer_class = Rider_serializer
    permission_classes = (IsAuthenticated,)
    queryset = Rider_serializer.Meta.model.objects.all()  

class Comment_viewsets (viewsets.ModelViewSet):
    serializer_class = Comment_serializer
    permission_classes = (IsAuthenticated,)
    queryset = Comment_serializer.Meta.model.objects.all()  
