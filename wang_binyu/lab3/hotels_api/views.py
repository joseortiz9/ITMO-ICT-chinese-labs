from rest_framework import generics, permissions, views, status
from rest_framework.response import Response

from hotels_api.models import Hotel, Room, Reservation, Comment
from hotels_api.serializers import HotelSerializer, RoomSerializer, ReservationSerializer, CommentSerializer


class HotelListView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelRoomsView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, hotel_id):
        rooms = Room.objects.filter(hotel=hotel_id).order_by('-created_at')
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)


class RoomListView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomCommentsView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, room_id):
        comments = Comment.objects.filter(room=room_id).order_by('-created_at')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, room_id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator_id=request.user.id, room_id=room_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservationsView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        reservations = Reservation.objects.filter(costumer=request.user.id).order_by('-created_at')
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)


class ReservationsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
