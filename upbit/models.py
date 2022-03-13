from django.db import models


# Create your models here.

class CandleChartModel(models.Model):
    market = models.CharField(max_length=15)
    candle_date_time_utc = models.DateTimeField()
    candle_date_time_kst = models.DateTimeField()
    opening_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    trade_price = models.FloatField()
    timestamp = models.FloatField()
    candle_acc_trade_price = models.FloatField()
    candle_acc_trade_volume = models.FloatField()
    unit = models.IntegerField()

    class Meta:
        unique_together = (("market", 'candle_date_time_kst'),)


class MarketTickerModel(models.Model):
    market = models.CharField(max_length=15, primary_key=True)
    korean_name = models.CharField(max_length=15)
    english_name = models.CharField(max_length=15)


class TradeTickModel(models.Model):
    market = models.CharField(max_length=15)
    trade_date_utc = models.CharField(max_length=15)
    trade_time_utc = models.CharField(max_length=10)
    timestamp = models.IntegerField()
    trade_price = models.FloatField()
    trade_volume = models.FloatField()
    prev_closing_price = models.FloatField()
    change_price = models.FloatField()
    ask_bid = models.CharField(max_length=5)
    sequential_id = models.IntegerField()

    class Meta:
        unique_together = (("market", "trade_date_utc", "trade_time_utc"),)
