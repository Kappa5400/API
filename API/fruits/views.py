from django.shortcuts import render
from rest_framework import generics
from .models import fruit
from .serializers import fruitserial


class fruit_list(generics.ListAPIView):
    queryset = fruit.objects.all()
    serializer_class = fruitserial

class fruit_crud(generics.RetrieveUpdateDestroyAPIView):
    queryset = fruit.objects.all()
    serializer_class = fruitserial
    lookup_field = "pk"
