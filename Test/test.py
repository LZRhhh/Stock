from alpha_vantage.timeseries import TimeSeries
from models import *

ts = TimeSeries(key='Y2617R1QN0XGOBFN')
# Get json object with the intraday data and another with  the call's metadata


# symbols = ['MSFT', 'GOOG']
# for symbol in symbols:
#     data, meta_data = ts.get_intraday(symbol=symbol, interval='1min')
#     for time in data:
#         print(symbol, time, data[time]['4. close'], data[time]['5. volume'])
#         realtime_data = RealtimeData(symbol=symbol, time=time, price=data[time]['4. close'], volume=data[time]['5. volume'])
#         realtime_data.save()

    # try:
    #     stock.save()
    #     print('Stock %s created' % symbol)
    # except:
    #     print('Stock %s duplicated' % symbol)


# historical
data, meta_data = ts.get_daily(symbol='MSFT')

for stock in data:
    print(stock, data[stock])

