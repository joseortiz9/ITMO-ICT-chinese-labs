from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


ROOM_TYPES = [
        ('1', '1 Single'),
        ('2', '2 Double'),
        ('3', '3 Deluxe'),
        ('4', '4 Presidential')
    ]


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.name, self.created_at)


class Room(models.Model):
    room_number = models.IntegerField(unique=True)
    type = models.CharField(max_length=1, choices=ROOM_TYPES, default=ROOM_TYPES[0])
    price = models.FloatField(default=0, validators=[MinValueValidator(0)])
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    guests = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}, {}, {}".format(self.room_number, self.get_type_display(), self.price, self.created_at)


class Comment(models.Model):
    text = models.CharField(max_length=255)
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    start_date = models.DateField()
    finish_date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
