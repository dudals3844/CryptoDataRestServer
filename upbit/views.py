from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
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

    def create(self, request, *args, **kwargs):
        candle_data = request.data
        serializer = self.get_serializer(data=candle_data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()


class MarketTickerView(viewsets.ModelViewSet):
    queryset = MarketTickerModel.objects.all()
    serializer_class = MarketTickerSerializer


class TradeTickView(viewsets.ModelViewSet):
    queryset = TradeTickModel.objects.all()
    serializer_class = TradeTickSerializer
    pagination_class = PostPageNumberPagination
