from django.views.generic import FormView
from record_trades.forms import CreateNewTradeForm


class CreateNewTradeView(FormView):
    """
    Records transaction when a new trade is placed

    ``Trade``
        An instance of :model:`record_trades.Trade`.

    **Template:**
    """
    template_name = '../templates/index.html'
    form_class = CreateNewTradeForm
    success_url = '/record'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
