from django.test import TestCase

# Create your tests here.
from alpha_vantage.timeseries import TimeSeries
from models import *

ts = TimeSeries(key='Y2617R1QN0XGOBFN')



symbols = ['MSFT', 'GOOG']
for symbol in symbols:
    data, meta_data = ts.get_intraday(symbol=symbol, interval='1min')
    for time in data:
        realtime_data = RealtimeData(symbol=symbol,
                                     time=time,
                                     price=data[time]['4. close'],
                                     volume=data[time]['5. volume'])
    realtime_data.save()


# # historical
# data, meta_data = ts.get_daily(symbol='MSFT')
#
# for stock in data:
#     print(stock, data[stock])
# print(meta_data)
