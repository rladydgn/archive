from rest_framework import serializers
from base.models import Driver, Pedestrian


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class PedestrianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedestrian
        fields = "__all__"
