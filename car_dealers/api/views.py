from rest_framework import generics

from .models import Dealer, Car
from .serializers import *


class DealerCreateView(generics.CreateAPIView):
    serializer_class = DealerDetailSerializer


class DealerListView(generics.ListAPIView):
    serializer_class = DealerDetailSerializer
    queryset = Dealer.objects.all()


class DealerDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = DealerDetailSerializer
    queryset = Dealer.objects.all()


class DealerDestroyView(generics.DestroyAPIView):
    serializer_class = DealerDetailSerializer
    queryset = Dealer.objects.all()


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()


class CarDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()


class CarSellView(generics.DestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
