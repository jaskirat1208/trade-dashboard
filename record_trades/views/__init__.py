"""
Displays the main index page for trade_record application
"""

from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    """
    Display an individual :model:`record_trades.Trade`.

    **Context**

    ``Trade``
        An instance of :model:`record_trades.Trade`.

    **Template:**

    :template:`myapp/my_template.html`
    """

    return HttpResponse("Hello, world. You're at the polls indexes.")
