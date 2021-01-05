from django_tables2 import SingleTableView, LazyPaginator
import django_filters as filters

from record_trades.models import Trade
from record_trades.tables import ViewTradeTable


class GetAllTradesView(SingleTableView):
    """
        Displaying all trades as a table
    """
    model = Trade
    template_name = '../templates/get_all_trades.html'
    table_class = ViewTradeTable
    paginator_class = LazyPaginator


