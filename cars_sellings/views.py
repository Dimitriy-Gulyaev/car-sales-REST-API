from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class SaleViewSet(viewsets.ModelViewSet):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class DealerViewSet(viewsets.ModelViewSet):
    serializer_class = DealerSerializer
    queryset = Dealer.objects.all()
