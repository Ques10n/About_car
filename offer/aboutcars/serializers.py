from rest_framework import serializers
from .models import Car, Comment


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'