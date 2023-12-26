from .models import *
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Group
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Payment
        fields = "__all__"


class GroupNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']