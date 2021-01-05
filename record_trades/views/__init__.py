from django.shortcuts import HttpResponse
from .create_new_trade_view import CreateNewTradeView


# Create your views here.
def index(request):
    """
    Display an individual :model:`record_trades.Trade`.

    **Context**

    ``Trade``
        An instance of :model:`record_trades.Trade`.

    **Template:**
    """

    return HttpResponse("Hello, world. You're at the polls indexes.")
