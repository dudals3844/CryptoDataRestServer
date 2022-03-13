from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CandleChartView,
    MarketTickerView,
    TradeTickView,
)

router = DefaultRouter()
router.register('candle', CandleChartView)
router.register('ticker', MarketTickerView)
router.register('trades', TradeTickView)

urlpatterns = [
    path('', include(router.urls))
]
