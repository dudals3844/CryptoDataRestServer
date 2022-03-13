from django.shortcuts import render
from .models import (
    CandleChartModel,
    MarketTickerModel,
    TradeTickModel,
)
from .serializers import (
    CandleChartSerializer,
    MarketTickerSerializer,
    TradeTickSerializer,
)
from .pagination import PostPageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class CandleChartView(viewsets.ModelViewSet):
    queryset = CandleChartModel.objects.all()
    serializer_class = CandleChartSerializer
    pagination_class = PostPageNumberPagination


class MarketTickerView(viewsets.ModelViewSet):
    queryset = MarketTickerModel.objects.all()
    serializer_class = MarketTickerSerializer


class TradeTickView(viewsets.ModelViewSet):
    queryset = TradeTickModel.objects.all()
    serializer_class = TradeTickSerializer
    pagination_class = PostPageNumberPagination
