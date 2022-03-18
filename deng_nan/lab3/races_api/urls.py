"""lab3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from races_api.views import RaceDetailView, RaceListView, RidersListView, RidersDetailView, RaceCommentsView, \
    TeamListView

urlpatterns = [
    path('teams', TeamListView.as_view()),

    path('races', RaceListView.as_view()),
    path('races/<int:pk>', RaceDetailView.as_view()),
    path('races/<int:race_id>/comments', RaceCommentsView.as_view()),

    path('riders', RidersListView.as_view()),
    path('riders/<int:pk>', RidersDetailView.as_view()),
]
