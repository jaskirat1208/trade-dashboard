from .create_new_trade_view import CreateNewTradeView
from .get_all_trades_view import GetAllTradesView
from django.shortcuts import redirect


def index(request):
    response = redirect('/record/add_trade')
    return response
