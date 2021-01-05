import logging

from django.views.generic import FormView
from record_trades.forms import CreateNewTradeForm


class CreateNewTradeView(FormView):
    """
    Records transaction when a new trade is placed

    ``Trade``
        An instance of :model:`record_trades.Trade`.

    **Template:**

    """
    template_name = '../templates/create_new_trade.html'
    form_class = CreateNewTradeForm
    success_url = '/record/get_all_trades'
    logger = logging.getLogger('trade.record')

    def form_valid(self, form):
        """ If form is valid, update the model
        :param form: CreateNewTradeForm
        :return:
        """
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        self.logger.info("Inputs are Valid. Updating records")
        form.save()
        return super().form_valid(form)

