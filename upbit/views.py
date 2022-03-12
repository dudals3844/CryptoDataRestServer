from django.shortcuts import render
from .models import (
    CandleChartModel,
)
from .serializers import (
    CandleChartSerializer,
)
from .pagination import PostPageNumberPagination
from rest_framework import viewsets


# Create your views here.

class CandleChartView(viewsets.ModelViewSet):
    queryset = CandleChartModel.objects.all()
    serializer_class = CandleChartSerializer
    pagination_class = PostPageNumberPagination
