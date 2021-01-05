from django.views.generic import FormView
from record_trades.forms import CreateNewTradeForm


class CreateNewTradeView(FormView):
    template_name = '../templates/index.html'
    form_class = CreateNewTradeForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)