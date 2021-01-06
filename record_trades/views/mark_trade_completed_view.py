import logging

from django.shortcuts import redirect
from django.views.generic import FormView

from record_trades.models import Trade


def MarkTradeComplete(request, trade_id):
    """
    Updates action_taken variable to True for a trade with action required

    ``Validation checks``
        - Update only if trade status is ``ACTION REQUIRED``

    :param request: Get request sent by browser
    :param trade_id: id parameter
    :return: redirect to home
    """

    logger = logging.getLogger('trade.record')
    logger.info('Updating trade with id: ' + trade_id)
    trade = Trade.objects.get(id=trade_id)
    trade.action_taken = True
    trade.save()
    logger.info(trade)
    return redirect('/')


