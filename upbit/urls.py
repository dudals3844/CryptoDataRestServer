from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CandleChartView,
    MarketTickerView,
)

router = DefaultRouter()
router.register('candle', CandleChartView)
router.register('ticker', MarketTickerView)

urlpatterns = [
    path('', include(router.urls))
]
