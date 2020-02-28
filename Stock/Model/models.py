from django.db import models


# Create your models here.
class RealtimeData(models.Model):
    symbol = models.CharField(max_length=5)
    time = models.DateTimeField(default='2020-01-01 00:00:00')
    price = models.FloatField(default=0)
    volume = models.IntegerField(default=0)


class HistoricalData(models.Model):
    symbol = models.CharField(max_length=5)
    date = models.DateField(default='2020-01-01')
    open = models.FloatField(default=0)
    high = models.FloatField(default=0)
    low = models.FloatField(default=0)
    close = models.FloatField(default=0)
    volume = models.IntegerField(default=0)
