from django.db import models


class Trade(models.Model):
    """ Means by which trades are stored in a database
    """
    id = models.AutoField(primary_key=True)
    trade_date = models.DateField('Trade Start Date')
    expiry_date = models.DateField('Trade End Date')
    strike = models.FloatField('Strike')
    yield_rate = models.FloatField('Yield(%)')
    b_ccy = models.CharField(max_length=10)
    alt_ccy = models.CharField(max_length=10)
    notional = models.IntegerField('Notional')