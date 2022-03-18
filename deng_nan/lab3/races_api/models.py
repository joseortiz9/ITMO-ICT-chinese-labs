from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Team(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.name, self.created_at)


class Rider(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True)
    car_description = models.CharField(max_length=200, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Race(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    winner = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='rider_winner', blank=True, null=True)
    riders = models.ManyToManyField(Rider)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.name, self.start_time)


class Comment(models.Model):
    text = models.CharField(max_length=255)
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.text, self.rating)
