from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator



class Conference(models.Model):
    name = models.CharField(max_length=200)
    topics = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    date = models.DateField()
    description_conference = models.CharField(max_length=200)
    description_venue = models.CharField(max_length=200)
    conditions = models.CharField(max_length=200)
    
    
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Presentation(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    recommended_for_publication = models.BooleanField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.author, self.conference.name)

class Comment(models.Model):
    text = models.CharField(max_length=500)
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
