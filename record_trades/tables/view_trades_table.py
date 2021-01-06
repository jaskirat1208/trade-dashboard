import itertools

import django_tables2 as tables

import constants
from record_trades.models import Trade


class ViewTradeTable(tables.Table):

    row_number = tables.Column(empty_values=(), orderable=False)
    status = tables.TemplateColumn(
        orderable=False, template_name='../templates/complete_trade_btn.html',
        extra_context={
            'active': constants.TRADE_TYPE_ACTIVE,
            'complete': constants.TRADE_TYPE_COMPLETED,
            'action_req': constants.TRADE_TYPE_ACTION_REQUIRED
        }
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = itertools.count()

    class Meta:
        model = Trade
        template_name = 'django_tables2/semantic.html'
        row_attrs = {
            "data-id": lambda record: record.pk
        }
        exclude = ('id', 'action_taken')

    def render_row_number(self):
        return next(self.counter)
