from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
import json

from foil import serializers

from Model.models import *
from alpha_vantage.timeseries import TimeSeries


def realtime(request, symbol):
    # ts = TimeSeries(key='Y2617R1QN0XGOBFN')
    realtime_data = RealtimeData.objects.filter(symbol=symbol)
    result = {'symbol': symbol, 'data': []}
    for data in realtime_data:
        data = model_to_dict(data)
        result['data'].append(data)
    # print(result)
    return JsonResponse(result)


def save_realtime(request, symbol):
    ts = TimeSeries(key='Y2617R1QN0XGOBFN')

    data, _ = ts.get_intraday(symbol=symbol, interval='1min')
    for time in data:
        realtime_data = RealtimeData(symbol=symbol,
                                     time=time,
                                     price=data[time]['4. close'],
                                     volume=data[time]['5. volume'])
        realtime_data.save()

    return HttpResponse("<p>Stock data saved!</p>")


def historical(request, symbol):
    # ts = TimeSeries(key='Y2617R1QN0XGOBFN')
    historical_data = HistoricalData.objects.filter(symbol=symbol)
    result = {'symbol': symbol, 'data': []}
    for data in historical_data:
        data = model_to_dict(data)
        result['data'].append(data)
    # print(result)
    return JsonResponse(result)


def save_historical(request, symbol):
    ts = TimeSeries(key='Y2617R1QN0XGOBFN')

    data, _ = ts.get_daily(symbol=symbol)
    for date in data:
        historical_data = HistoricalData(symbol=symbol,
                                         date=date,
                                         open=data[date]['1. open'],
                                         high=data[date]['2. high'],
                                         low=data[date]['3. low'],
                                         close=data[date]['4. close'],
                                         volume=data[date]['5. volume'])
        historical_data.save()

    return HttpResponse("<p>Stock data saved!</p>")
