from django import forms
from .models import Comment, COMMENT_TYPES, RIDER_CLASS_TYPES, Team, Rider
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    text = forms.CharField(label="Comment", required=True)
    rating = forms.IntegerField(label="Rating", max_value=10, min_value=0, required=True)
    type = forms.ChoiceField(label="Type", required=True, choices=COMMENT_TYPES)

    class Meta:
        model = Comment
        fields = ["text", "rating", "type"]


class UserForm(forms.ModelForm):
    username = forms.CharField(label="username")
    password = forms.CharField(widget=forms.PasswordInput(), label="password")
    email = forms.CharField(label="Email address")
    first_name = forms.CharField(label="first_name")
    last_name = forms.CharField(label="last_name")

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')


class RiderForm(forms.ModelForm):
    first_name = forms.CharField(label="First name", required=True)
    last_name = forms.CharField(label="Last name", required=True)
    description = forms.CharField(label="Description")
    experience = forms.CharField(label="Experience")
    class_type = forms.ChoiceField(label="Class type", required=True, choices=RIDER_CLASS_TYPES)
    car_description = forms.CharField(label="Car Description")
    team_id = forms.ModelChoiceField(queryset=Team.objects.all(), label="Team")

    class Meta:
        model = Rider
        fields = ('first_name', 'last_name', 'description', 'experience', 'class_type', 'car_description', 'team_id')
