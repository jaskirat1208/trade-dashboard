import logging

from django_tables2 import SingleTableView, LazyPaginator

import constants
from record_trades.models import Trade
from record_trades.tables import ViewTradeTable


class GetAllTradesView(SingleTableView):
    """
        Displaying all trades as a table
    """
    logger = logging.getLogger('trade.record')
    model = Trade
    template_name = '../templates/get_all_trades.html'
    table_class = ViewTradeTable
    paginator_class = LazyPaginator

    def get_queryset(self):
        """
        Gets queryset from the database. Filters it on the basis of status
        :return: Filtered trades
        """
        trade_status = self.kwargs.get('status')
        self.logger.info(trade_status)
        trades = Trade.objects.all()

        if trade_status == 'ALL':
            self.logger.info('Fetching all trades')
            return trades

        self.logger.info(constants.TRADE_STATUS_LIST)
        if trade_status not in constants.TRADE_STATUS_LIST:
            self.logger.info('Invalid trade status ' + trade_status + '. Showing all elements')
            return trades

        return [x for x in trades if x.status == trade_status]

