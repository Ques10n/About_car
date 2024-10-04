from rest_framework.permissions import IsAuthenticated

from .models import Car, Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from .serializers import ItemSerializer, CommentSerializer


class ItemList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Car.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Item(APIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get(self, request, id= None):
        car_id = self.kwargs.get('id')
        items = Car.objects.filter(id=id)
        if items.exists():
            serializer = ItemSerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)


    def put(self, request, id=None):
        car_id = self.kwargs.get('id')
        item = Car.objects.get(id=car_id)
        serializer = ItemSerializer(item, data=request.data, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, id=None):
        car_id = self.kwargs.get('id')
        try:
            item = Car.objects.get(id=car_id)
            item.delete()
            return Response({"detail": "Deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Car.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)


class CommentList(APIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get(self, request, id= None):
        car = Car.objects.get(id=id)
        comments = Comment.objects.filter(car=car)
        if comments.exists():
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "Car not found."}, status=status.HTTP_404_NOT_FOUND)


    def post(self, request, id= None):
        car = Car.objects.get(id=id)
        data = request.data.copy()
        data['car'] = car.id
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
