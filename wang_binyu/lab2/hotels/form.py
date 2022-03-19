from django import forms
from django.contrib.auth.models import User

from lab2 import settings
from .models import Comment


class CommentForm(forms.ModelForm):
    text = forms.CharField(label="Comment", required=True)
    rating = forms.IntegerField(label="Rating", max_value=10, min_value=1, required=True)
    start_date = forms.DateField(label="Begin day", required=True, input_formats=settings.DATE_INPUT_FORMATS,
                                 widget=forms.DateInput(format='%d/%m/%Y', attrs={
                                     'class': 'form-control datetimepicker-input',
                                     'type': 'date',
                                     'placeholder': '28/01/2022',
                                     'data-target': '#datetimepicker1'
                                 }))
    finish_date = forms.DateField(label="Finish day", required=True, input_formats=settings.DATE_INPUT_FORMATS,
                                  widget=forms.DateInput(format='%d/%m/%Y', attrs={
                                      'class': 'form-control datetimepicker-input',
                                      'type': 'date',
                                      'placeholder': '29/01/2022',
                                      'data-target': '#datetimepicker2'
                                  }))

    class Meta:
        model = Comment
        fields = ["text", "rating", "start_date", "finish_date"]


class UserForm(forms.ModelForm):
    username = forms.CharField(label="username")
    password = forms.CharField(widget=forms.PasswordInput(), label="password")
    email = forms.CharField(label="Email address")
    first_name = forms.CharField(label="first_name")
    last_name = forms.CharField(label="last_name")

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
