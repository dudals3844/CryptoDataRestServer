from django.shortcuts import render
from .models import (
    CandleChartModel,
    MarketTickerModel,
)
from .serializers import (
    CandleChartSerializer,
    MarketTickerSerializer,
)
from .pagination import PostPageNumberPagination
from rest_framework import viewsets


# Create your views here.

class CandleChartView(viewsets.ModelViewSet):
    queryset = CandleChartModel.objects.all()
    serializer_class = CandleChartSerializer
    pagination_class = PostPageNumberPagination


class MarketTickerView(viewsets.ModelViewSet):
    queryset = MarketTickerModel.objects.all()
    serializer_class = MarketTickerSerializer
