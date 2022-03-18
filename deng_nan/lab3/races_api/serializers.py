from django.contrib.auth.models import User
from rest_framework import serializers

from races_api.models import Race, Rider, Team, Comment


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id", "last_login", "is_superuser", "first_name", "username",
            "last_name", "email", "is_staff", "is_active", "date_joined"
        )


class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = ("id", "name", "description", "car_description", "creator_id", "team_id", "created_at", "updated_at")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['creator'] = CustomUserSerializer(User.objects.get(pk=representation['creator_id'])).data
        representation['team'] = TeamSerializer(Team.objects.get(pk=representation['team_id'])).data
        return representation


class RaceSerializer(serializers.ModelSerializer):
    creator = CustomUserSerializer()
    winner = RiderSerializer()
    riders = RiderSerializer(many=True)

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


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "text", "rating", "creator_id", "race_id", "created_at", "updated_at")
        read_only_fields = []

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['creator'] = CustomUserSerializer(User.objects.get(pk=representation['creator_id'])).data
        return representation
