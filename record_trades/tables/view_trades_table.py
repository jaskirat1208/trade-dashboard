import django_tables2 as tables
from record_trades.models import Trade


class ViewTradeTable(tables.Table):
    class Meta:
        model = Trade
        template_name = 'django_tables2/bootstrap.html'
