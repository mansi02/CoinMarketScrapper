from django.shortcuts import render
from rest_framework import generics
from .serializers import MarketCap, MarketCapSerializer
# Create your views here.
class MarketCapView(generics.ListCreateAPIView):
    queryset= MarketCap.objects.all()
    serializer_class = MarketCapSerializer
