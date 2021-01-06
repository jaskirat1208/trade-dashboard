import logging

from django.shortcuts import redirect
from django.views.generic import View

import constants
from record_trades.models import Trade


class MarkTradeComplete(View):
    """
    Updates action_taken variable to True for a trade with action required

    ``Validation checks``
       - Update only if trade status is ``ACTION REQUIRED``

    :param request: Get request sent by browser
    :param trade_id: trade id to update complete
    :return: redirect to home
    """
    logger = logging.getLogger('trade.record')

    def trade_valid(self, trade):
        if trade.status == constants.TRADE_TYPE_ACTION_REQUIRED:
            self.logger.info('No action required on this trade')
            return True

        self.logger.info('Trade can be marked complete')
        return False

    def get(self, request, trade_id):
        """
        Updates action_taken variable to True for a trade with action required

        ``Validation checks``
           - Update only if trade status is ``ACTION REQUIRED``

        :param request: Get request sent by browser
        :param trade_id: trade id to update complete
        :return: redirect to home
        """

        self.logger.info('Updating trade with id: ' + trade_id)
        trade = Trade.objects.get(id=trade_id)
        if self.trade_valid(trade):
            trade.action_taken = True
            trade.save()
            self.logger.info('Trade updated successfully')
            # TODO CREATE DIALOG BOX STATING SUCCESSFUL UPDATION
            return redirect('/')

        # TODO CREATE A DIALOG BOX STATING UNSUCCESSFUL UPDATION
        return redirect('/')
