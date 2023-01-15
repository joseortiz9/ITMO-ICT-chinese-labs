from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
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

class Comment_type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Rider_class_type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Rider(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    rider_description = models.CharField(max_length=500, null=True)
    car_description = models.CharField(max_length=500, null=True)
    rider_experience = models.CharField(max_length=500, null=True)
    class_type = models.ForeignKey(Rider_class_type, on_delete=models.CASCADE, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Race(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.DateTimeField(blank=True, null=True)
    winner = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='rider_winner', blank=True, null=True)
    riders = models.ManyToManyField(Rider)

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.name, self.start_time)


class Comment(models.Model):
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    text = models.CharField(max_length=500)
    type = models.ForeignKey(Comment_type, on_delete=models.CASCADE, null=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
