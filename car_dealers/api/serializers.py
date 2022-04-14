from rest_framework import serializers

from .models import Dealer, Car


class DealerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = '__all__'


class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('vin', 'brand', 'car_model',)
