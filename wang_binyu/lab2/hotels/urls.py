"""lab2 URL Configuration

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
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hotels', views.hotels, name='hotels'),
    path('hotels/<int:hotel_id>', views.hotel_details, name='hotel_details'),
    path('rooms', views.user_rooms, name='user_rooms'),
    path('rooms/<int:room_id>', views.room_details, name='room_details'),
    path('login', views.user_login, name='user_login'),
    path('register', views.user_register, name='user_register'),
    path('logout1', views.user_logout, name='user_logout'),
]
