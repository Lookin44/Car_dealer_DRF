from rest_framework import viewsets

from .models import Car, Dealer
from .serializers import CarSerializer, DealerSerializer


class CarViewSets(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class DealerViewSets(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
