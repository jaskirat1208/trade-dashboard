import itertools

import django_tables2 as tables
from django.utils.html import format_html

import constants
from record_trades.models import Trade


class ViewTradeTable(tables.Table):
    status_color_map = {
        constants.TRADE_TYPE_ACTIVE: 'badge badge-primary',
        constants.TRADE_TYPE_COMPLETED: 'badge badge-primary',
        constants.TRADE_TYPE_ACTION_REQUIRED: 'badge badge-warning'
    }

    row_number = tables.Column(empty_values=(), orderable=False)
    status = tables.Column('Status', orderable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = itertools.count()

    class Meta:
        model = Trade
        template_name = 'django_tables2/semantic.html'
        row_attrs = {
            "data-id": lambda record: record.pk
        }
        exclude = ('id',)

    def render_row_number(self):
        return next(self.counter)

    def render_status(self, value):
        return format_html('<span class="{}">{}</span>', self.status_color_map[value], value)