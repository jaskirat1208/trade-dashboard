from django.db import models
from django.utils import timezone


# Create your models here.
class Trade(models.Model):
    id = models.AutoField(primary_key=True)
    trade_date = models.DateField('Trade Start Date')
    expiry_date = models.DateField('Trade End Date')
    strike = models.FloatField('Strike')
    yield_rate = models.FloatField('Yield(%)')
    b_ccy = models.CharField(max_length=10)
    alt_ccy = models.CharField(max_length=10)
    notional = models.IntegerField('Notional')

    # def __init__(self, trade_date, expiry_date, strike, yield_rate, b_ccy, alt_ccy, notional):
    #     super().__init__()
    #     self.trade_date = trade_date
    #     self.expiry_date = expiry_date
    #     self.strike = strike
    #     self.yield_rate = yield_rate
    #     self.b_ccy = b_ccy
    #     self.alt_ccy = alt_ccy
    #     self.notional = notional
