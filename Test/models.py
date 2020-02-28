from mongoengine import *

connect('test')


class RealtimeData(Document):
    symbol = StringField(required=True)
    time = DateTimeField(required=True)
    price = FloatField(required=True)
    volume = IntField(required=True)


class HistoricalData(Document):
    symbol = StringField(required=True)
    date = DateField(required=True)
    open = FloatField(required=True)
    high = FloatField(required=True)
    low = FloatField(required=True)
    close = FloatField(required=True)
    volume = IntField(required=True)

