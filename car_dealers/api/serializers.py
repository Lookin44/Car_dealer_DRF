from rest_framework import serializers

from .models import Car, Dealer


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'vin', 'brand')


class DealerSerializer(serializers.ModelSerializer):

    cars = CarDetailSerializer(many=True)

    class Meta:
        model = Dealer
        fields = ('name', 'address', 'cars',)
