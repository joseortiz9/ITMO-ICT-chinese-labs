from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"


class ReaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reader
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    book_name = serializers.CharField(max_length=240)
    Type = serializers.CharField(max_length=120)
    year_of_pub = serializers.DateField()

    def create(self, validated_data):
        book = Book(**validated_data)
        book.save()
        return Book(**validated_data)


class ReaderCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=240)
    last_name = serializers.CharField(max_length=240)
    sex = serializers.CharField(max_length=120)
    birthday = serializers.DateField()

    def create(self, validated_data):
        reader = Reader(**validated_data)
        reader.save()
        return Reader(**validated_data)


class BookSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    book_name = serializers.CharField(max_length=240)
    Type = serializers.CharField(max_length=120)
    year_of_pub = serializers.DateField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.book_name = validated_data.get('book_name', instance.book_name)
        instance.Type = validated_data.get('Type', instance.Type)
        instance.id = validated_data.get('id', instance.id)
        instance.year_of_pub = validated_data.get('year_of_pub', instance.year_of_pub)
        instance.save()
        return instance


class ReaderSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=240)
    last_name = serializers.CharField(max_length=240)
    sex = serializers.CharField(max_length=120)
    birthday = serializers.DateField()

    def create(self, validated_data):
        return Reader.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.id = validated_data.get('id', instance.id)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.save()
        return instance
