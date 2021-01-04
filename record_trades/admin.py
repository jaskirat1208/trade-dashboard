from django.contrib import admin

from .models import Trade


# Register your models here.
class TradeAdmin(admin.ModelAdmin):
    empty_value_display = ''
    fields = ('trade_date', 'expiry_date', 'b_ccy', 'alt_ccy', 'strike', 'yield_rate', 'notional')
    list_display = ('id', 'trade_date', 'expiry_date', 'ccy', 'strike', 'yield_rate', 'notional')

    @staticmethod
    def ccy(obj):
        return str.format('{}-{}', obj.b_ccy, obj.alt_ccy)


admin.site.register(Trade, TradeAdmin)
