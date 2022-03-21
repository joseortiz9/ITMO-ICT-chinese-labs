from rest_framework import generics, status
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response

# Create your views here.


class BookAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({"books": serializer.data})


class BookCreateAPIView(APIView):
    serializer_class = BookCreateSerializer
    queryset = Book.objects.all()

    def post(self, request):

        print("REQUEST DATA", request.data)
        book = request.data.copy()
        print("PROF DATA", book)
        serializer = BookCreateSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response({"Success": "Book '{}' created succesfully.".format(book_saved.book_name)})


class BookView(APIView):
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        ser = BookSerializers(instance=book)
        return Response(ser.data)

    def put(self, request, pk):  # 修改
        book = Book.objects.get(pk=pk)
        ser = BookSerializers(instance=book, data=request.data)  # 注意指定参数
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=200)
        return Response(ser.errors)

    def delete(self, request, pk):
        Book.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_200_OK)


class ReaderAPIView(APIView):
    def get(self, request):
        readers = Reader.objects.all()
        serializer = ReaderSerializer(readers, many=True)
        return Response({"readers": serializer.data})


class ReaderCreateAPIView(APIView):
    serializer_class = ReaderCreateSerializer
    queryset = Reader.objects.all()

    def post(self, request):

        print("REQUEST DATA", request.data)
        book = request.data.copy()
        print("PROF DATA", book)
        serializer = ReaderCreateSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            reader_saved = serializer.save()
        return Response({"Success": "Reader '{}' created succesfully.".format(reader_saved.first_name)})


class ReaderView(APIView):
    def get(self, request, pk):
        reader = Reader.objects.get(id=pk)
        ser = ReaderSerializers(instance=reader)
        return Response(ser.data)

    def put(self, request, pk):  # 修改
        reader = Reader.objects.get(pk=pk)
        ser = ReaderSerializers(instance=reader, data=request.data)  # 注意指定参数
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=200)
        return Response(ser.errors)

    def delete(self, request, pk):
        Reader.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_200_OK)
