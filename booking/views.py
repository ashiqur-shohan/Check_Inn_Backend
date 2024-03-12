from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookingSerializers
from .models import Booking
# Create your views here.

class BookingViewset(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    