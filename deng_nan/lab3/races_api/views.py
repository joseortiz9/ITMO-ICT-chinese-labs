from rest_framework import generics, views, status, permissions
from rest_framework.response import Response

from races_api.models import Race, Rider, Comment
from races_api.serializers import RaceSerializer, RiderSerializer, CommentSerializer


class RaceListView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Race.objects.all()
    serializer_class = RaceSerializer


class RaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Race.objects.all()
    serializer_class = RaceSerializer


class RaceCommentsView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, race_id):
        comments = Comment.objects.filter(race=race_id).all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, race_id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator_id=request.user.id, race_id=race_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RidersListView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer

    def perform_create(self, serializer):
        serializer.save(creator_id=self.request.user.id, team_id=int(serializer.initial_data['team_id']))


class RidersDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer
