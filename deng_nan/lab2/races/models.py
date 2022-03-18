from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


COMMENT_TYPES = [
        ('1', 'вопрос о сотрудничестве'),
        ('2', 'вопрос о гонках'),
        ('3', 'иное'),
    ]


RIDER_CLASS_TYPES = [
        ('1', 'A junior'),
        ('2', 'B middle'),
        ('3', 'C senior'),
    ]


class Team(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.name, self.created_at)


class Rider(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True)
    experience = models.CharField(max_length=200, null=True)
    class_type = models.CharField(max_length=1, choices=RIDER_CLASS_TYPES, default=RIDER_CLASS_TYPES[0])
    car_description = models.CharField(max_length=200, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Race(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    winner = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='rider_winner', blank=True, null=True)
    riders = models.ManyToManyField(Rider)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.name, self.start_time)


class Comment(models.Model):
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    text = models.CharField(max_length=255)
    type = models.CharField(max_length=1, choices=COMMENT_TYPES, default=COMMENT_TYPES[0])
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
