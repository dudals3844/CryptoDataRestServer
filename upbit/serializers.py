from rest_framework import serializers
from .models import (
    CandleChartModel,
    MarketTickerModel,
    TradeTickModel,
)


class CandleChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandleChartModel
        fields = "__all__"


class MarketTickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketTickerModel
        fields = '__all__'


class TradeTickSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeTickModel
        fields = "__all__"
