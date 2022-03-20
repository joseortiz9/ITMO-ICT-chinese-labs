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

from hotels_api.views import HotelListView, RoomListView, HotelRoomsView, ReservationsView, ReservationsDetailsView, \
    RoomCommentsView, HotelDetailsView, RoomDetailsView, RoomReservationView

urlpatterns = [
    path('hotels', HotelListView.as_view()),
    path('hotels/<int:pk>', HotelDetailsView.as_view()),
    path('hotels/<int:hotel_id>/rooms', HotelRoomsView.as_view()),
    path('rooms', RoomListView.as_view()),
    path('rooms/<int:pk>', RoomDetailsView.as_view()),
    path('rooms/<int:room_id>/reserved', RoomReservationView.as_view()),
    path('rooms/<int:room_id>/comments', RoomCommentsView.as_view()),
    path('reservations', ReservationsView.as_view()),
    path('reservations/<int:pk>', ReservationsDetailsView.as_view()),
]
