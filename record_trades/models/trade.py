from django.db import models
from django.utils import timezone

import constants


class Trade(models.Model):
    """ Basic Structure of a trade
    """
    id = models.AutoField('Trade ID', primary_key=True)
    trade_date = models.DateField('Trade Start Date')
    expiry_date = models.DateField('Trade End Date')
    strike = models.FloatField('Strike', help_text='Ratio of primary vs secondary currency')
    yield_rate = models.FloatField('Yield(%)', help_text='Annualized Rate of Return')
    b_ccy = models.CharField('Base currency', max_length=10)
    alt_ccy = models.CharField('Alternate currency', max_length=10)
    notional = models.IntegerField('Notional', help_text='Assets affected by Trade')

    @property
    def status(self):
        """ Checks if any action is required by the trader

        ``Return Values``
            - ACTIVE when holding period is due
            - ACTION REQUIRED when holding period is over and user has not marked it complete
            - COMPLETE when holding period is over and user has marked it complete
        """

        now = timezone.now()
        if self.expiry_date < now.date():
            return constants.TRADE_TYPE_ACTION_REQUIRED

        return constants.TRADE_TYPE_ACTIVE
