from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HotelSerializers
from .models import Hotel
# Create your views here.

class HotelViewset(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers