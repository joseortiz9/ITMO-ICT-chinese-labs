from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .serializers import (
    User_serializer,Airline_serializer,Passenger_serializer,Review_serializer,Air_travel_serializer
)

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

# The Login class is an APIView that handles user authentication by accepting a username 
# and password in the request data, and using Django's built-in authenticate 
# function to check if the provided credentials are valid. If they are, a new token 
# is generated using Django Rest Framework's Token model and returned in the response. 
# If the credentials are invalid, an error message is returned.

class Login(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

# The Logout class is an APIView that handles user logout by deleting the current user's 
# authentication token, forcing the user to re-authenticate on their next request.
class Logout(APIView):
    def post(self, request):
        user = request.user
        if user.is_authenticated:
            # delete the token to force a login
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({"error": "user not authenticated"}, status=status.HTTP_400_BAD_REQUEST)

# The Airline_viewsets, Passenger_viewsets, Review_viewsets, User_viewsets, 
# and Air_travel_viewsets classes are all viewsets that inherit from Django 
# Rest Framework's ModelViewSet. They handle CRUD operations for their 
# respective models (Airline, Passenger, Review, User, and Air_travel) and 
# use serializers (Airline_serializer, Passenger_serializer, Review_serializer, 
# User_serializer, and Air_travel_serializer) to handle the data conversion between 
# the model and JSON. They also set the permission class to IsAuthenticated, meaning 
# that only authenticated user can access these viewsets.


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