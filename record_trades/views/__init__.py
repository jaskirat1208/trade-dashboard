from django.shortcuts import redirect

from .create_new_trade_view import CreateNewTradeView
from .get_all_trades_view import GetAllTradesView
from .mark_trade_completed_view import MarkTradeComplete


def index(request):
    """
    View created to redirect basic requests to add_trade url

    ``Redirected urls``
        - '/'
        - '/record'

    :param request: request from browser
    :return: redirect to /record/add_trade
    """
    response = redirect('/record/add_trade')
    return response
