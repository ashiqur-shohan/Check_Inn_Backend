from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ReviewSerializers
from .models import Review

# Create your views here.

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers