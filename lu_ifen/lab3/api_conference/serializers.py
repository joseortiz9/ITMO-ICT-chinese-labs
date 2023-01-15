# import serializers from the REST framework
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Conference, Presentation, Review
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# create a serializer class

class user_token (serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name')

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class Conference_serializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = '__all__'


class Presentation_serializer(serializers.ModelSerializer):
    class Meta:
        model = Presentation
        fields = '__all__'

class Review_serializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
