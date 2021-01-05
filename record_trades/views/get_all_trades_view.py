from django_tables2 import SingleTableView

from record_trades.models import Trade
from record_trades.tables import ViewTradeTable


class GetAllTradesView(SingleTableView):
    """
        Displaying all trades as a table
    """
    model = Trade
    template_name = '../templates/get_all_trades.html'
    table_class = ViewTradeTable
    # form_class = CreateNewTradeForm
    # logger = logging.getLogger('trade.record')
    #
    # def form_valid(self, form):
    #     """ If form is valid, update the model
    #     :param form: CreateNewTradeForm
    #     :return:
    #     """
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     self.logger.info("Inputs are Valid. Updating records")
    #     form.save()
    #     return super().form_valid(form)
