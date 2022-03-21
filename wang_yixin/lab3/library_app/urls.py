from django.urls import path
from .views import *
from rest_framework import permissions


app_name = "library_app"

urlpatterns = [
   path('books/', BookAPIView.as_view()),
   path('books/create/', BookCreateAPIView.as_view()),
   path('books/<int:pk>/', BookView.as_view()),
   path('authors/', AuthorAPIView.as_view()),
   path('authors/<int:pk>', AuthorDetailsView.as_view()),
   path('authors/<int:author_id>/books', AuthorBooksView.as_view()),
   path('readers/', ReaderAPIView.as_view()),
   path('readers/create/', ReaderCreateAPIView.as_view()),
   path('readers/<int:pk>/', ReaderView.as_view()),
]
