from django.contrib.auth.models import User
from rest_framework import serializers

from hotels_api.models import Hotel, Comment, Room, Reservation


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id", "last_login", "is_superuser", "first_name", "username",
            "last_name", "email", "is_staff", "is_active", "date_joined"
        )


class HotelSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer()

    class Meta:
        model = Hotel
        fields = ("id", "name", "owner", "created_at", "updated_at")


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("costumer_id", "room_id", "start_date", "finish_date", "created_at", "updated_at")

    def validate(self, attrs):
        if attrs['start_date'] > attrs['finish_date']:
            raise serializers.ValidationError("finish must occur after start")
        return attrs


class RoomSerializer(serializers.ModelSerializer):
    reservations = ReservationSerializer(many=True)

    class Meta:
        model = Room
        fields = (
            "id", "room_number", "type", "price", "hotel_id",
            "reservations", "created_at", "updated_at"
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "text", "rating", "creator_id", "room_id", "created_at", "updated_at")
        read_only_fields = []

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['creator'] = CustomUserSerializer(User.objects.get(pk=representation['creator_id'])).data
        return representation
