from rest_framework import serializers
from .models import (
    CandleChartModel,
)


class CandleChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandleChartModel
        fields = "__all__"
