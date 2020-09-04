from django.shortcuts import render
from rest_framework import viewsets
from .models import Car
from .serializers import CarSerializer

class CarView(viewsets.ModelViewSet):
    #specify how you will get the objects from db...using queryset
    queryset = Car.objects.all()
    #specify how to serialize these objects...using serializer class
    serializer_class = CarSerializer