from django.contrib import admin
from django.urls import path
from .views import MarketCapView

urlpatterns = [
    path('', MarketCapView.as_view(),name="market_cap"),
]
