from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (
    CustomTokenObtainPairSerializer, 
    user_token,Team_serializer,Race_serializer, 
    Comment_serializer, 
    Rider_serializer,
    Comment_serializer
)
from django.contrib.auth.models import User

# The Login class is based on TokenObtainPairView which provides a simple way 
# to handle JWT-based authentication. 

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(
            username=username,
            password=password
        )
        if user:
            login_serializer = self.serializer_class(data=request.data)
            if user.is_active:
                if login_serializer.is_valid():
                    user_serializer = user_token(user)
                    
                    return Response({
                        'token': login_serializer.validated_data.get('access'),
                        'refresh-token': login_serializer.validated_data.get('refresh'),
                        'user': user_serializer.data,
                        'message': 'Successful Login'
                    }, status=status.HTTP_200_OK)
                return Response({'error': 'wrong username or password'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'error': 'user not active'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'wrong username or password'}, status=status.HTTP_400_BAD_REQUEST)


# The Logout class is a GenericAPIView that handles user logout by 
# invalidating the user's refresh token. It's checking if the user exists 
# and if it exists it invalidates the user's refresh token.

class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user', 0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'logged out successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'user does not exist'}, status=status.HTTP_400_BAD_REQUEST)

# This code defines a Team_viewsets class that is based on Django 
# Rest Framework's ModelViewSet. It is used to handle CRUD operations 
# for the Team model.

# Team_viewsets uses Team_serializer to handle the data conversion between the 
# Team model and JSON. It sets the permission class to IsAuthenticated, meaning that 
# only authenticated users can access this viewset.

# It overrides the default create, destroy, list, update, partial_update, 
# and retrieve functions provided by the ModelViewSet to customize the behavior 
# of these actions.

class Team_viewsets (viewsets.ModelViewSet):
    serializer_class = Team_serializer
    permission_classes = (IsAuthenticated,)
    queryset = Team_serializer.Meta.model.objects.all()  

    # The create method is used to handle the creation of a new Team instance. 
    # It takes the request data, converts it to a serializer, validates the data, 
    # and saves it to the database. If successful, it returns the newly created Team 
    # data along with a status of 201 (CREATED).

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # The destroy method is used to handle the deletion of a Team instance. 
    # It takes the primary key of the instance to be deleted, fetches the 
    # instance from the database, and deletes it. If successful, it returns 
    # a status of 204 (NO CONTENT).

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # The list method is used to handle the retrieval of a list of all Team 
    # instances. It takes the queryset, applies any filters specified in the 
    # request, paginates the data if necessary, and returns the list of Teams.


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # The update method is used to handle the updating of a Team instance

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    # The partial_update method is used to handle partially updating a Team instance. 
    # It sets the partial argument to True and calls the update method with the provided arguments.
    # This allows for fields to be updated without having to provide all fields in the request.

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    # The retrieve method is used to handle the retrieval of a specific Team instance.
    # It takes the primary key of the instance to be retrieved, fetches the instance 
    # from the database, converts it to a serializer, and returns the data of the Team instance.

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
        
# It is the same for the other classes, they only differ in the model on which they are based

class Race_viewsets (viewsets.ModelViewSet):
    serializer_class = Race_serializer
    permission_classes = (IsAuthenticated,)
    queryset = Race_serializer.Meta.model.objects.all()  

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class Rider_viewsets (viewsets.ModelViewSet):
    serializer_class = Rider_serializer
    permission_classes = (IsAuthenticated,)
    queryset = Rider_serializer.Meta.model.objects.all()  

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class Comment_viewsets (viewsets.ModelViewSet):
    serializer_class = Comment_serializer
    permission_classes = (IsAuthenticated,)
    queryset = Comment_serializer.Meta.model.objects.all()  

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
