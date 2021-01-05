import logging

from django import forms

# Local imports
from record_trades.models import Trade


class CreateNewTradeForm(forms.ModelForm):
    name = forms.CharField()
    logger = logging.getLogger('trade.record')

    class Meta:
        model = Trade
        exclude = ()

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        self.logger.info("Sending a mail")
        pass

