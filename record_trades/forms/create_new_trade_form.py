import ccy
import logging

from django import forms

# Local imports
from record_trades.models import Trade


class CreateNewTradeForm(forms.ModelForm):
    """
    ``Form``
        A boilerplate form created with :model:`record_trades.Trade` as the underlying model
    """

    logger = logging.getLogger('trade.record')
    # Dates
    trade_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'})
    )

    expiry_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'})
    )

    # Form widget for currencies
    b_ccy = forms.ChoiceField(
        label='Base currency', choices=map(lambda r: (r, r), ccy.all()), help_text='Base currency unit'
    )
    alt_ccy = forms.ChoiceField(
        label='Alternate currency', choices=map(lambda r: (r, r), ccy.all()), help_text='Alternate currency'
    )

    class Meta:
        model = Trade
        exclude = ('action_taken',)

    def clean(self):
        """
        Performing validation checks and adds errors in place on the form:
            - Trade date < Expiry date
            - base and alt ccy should be different
            - Check if strike and notional are positive
        """
        self.logger.info('Performing validation checks')
        cleaned_data = super().clean()

        # Fetch elements from cleaned data
        trade_date = cleaned_data.get('trade_date')
        expiry_date = cleaned_data.get('expiry_date')
        b_ccy = cleaned_data.get('b_ccy')
        alt_ccy = cleaned_data.get('alt_ccy')
        strike = cleaned_data.get('strike')
        notional = cleaned_data.get('notional')

        self.logger.info('Checking for trade and expiry date')
        # Expiry date > trade date
        if expiry_date < trade_date:
            self.add_error('expiry_date', 'Expiry date should always be greater than trade date')

        self.logger.info('Comparing units of base and alternate currency')
        # Base and alt currency should be different
        if b_ccy == alt_ccy:
            self.add_error('alt_ccy', 'Alternate currency unit should be different from base currency')

        self.logger.info('Comparing strike and notionals')
        if strike < 0:
            self.add_error('strike', 'Strike conversion rate must be positive')

        if notional < 0:
            self.add_error('notional', 'Notional must be positive')
