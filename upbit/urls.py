from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CandleChartView,
)

router = DefaultRouter()
router.register('candle', CandleChartView)

urlpatterns = [
    path('', include(router.urls))
]
