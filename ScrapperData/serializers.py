from rest_framework import serializers
from .models import MarketCap

class MarketCapSerializer(serializers.ModelSerializer):
    class Meta:
        model =  MarketCap
        fields ='__all__'