# import serializers from the REST framework
from rest_framework import serializers
from django.contrib.auth.models import User
from api_race.models import Race, Rider, Team, Comment
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# create a serializer class

class user_token (serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name')

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class Team_serializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        

class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id", "last_login", "is_superuser", "first_name", "username",
            "last_name", "email", "is_staff", "is_active", "date_joined"
        )


class Rider_serializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = ("id", "name", "description", "car_description", "creator_id", "team_id", "created_at", "updated_at")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['creator'] = User_serializer(User.objects.get(pk=representation['creator_id'])).data
        representation['team'] = Team_serializer(Team.objects.get(pk=representation['team_id'])).data
        return representation


class Race_serializer(serializers.ModelSerializer):
    creator = User_serializer()
    winner = Rider_serializer()
    riders = Rider_serializer(many=True)

    class Meta:
        model = Race
        fields = (
            "id", "name", "description", "start_time", "finish_time",
            "creator", "winner", "riders", "created_at", "updated_at"
        )

    def validate(self, attrs):
        if attrs['start_time'] > attrs['finish_time']:
            raise serializers.ValidationError("finish must occur after start")
        return attrs


class Comment_serializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "text", "rating", "creator_id", "race_id", "created_at", "updated_at")
        read_only_fields = []

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['creator'] = User_serializer(User.objects.get(pk=representation['creator_id'])).data
        return representation