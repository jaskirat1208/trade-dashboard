import ccy

from django import forms

# Local imports
from record_trades.models import Trade


class CreateNewTradeForm(forms.ModelForm):
    """
    ``Form``
        A boilerplate form created with :model:`record_trades.Trade` as the underlying model
    """

    # Dates
    trade_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'})
    )

    expiry_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'})
    )

    # Form widget for currencies
    b_ccy = forms.ChoiceField(
        label='Base currency', choices=map(lambda r: (r, r), ccy.all()), help_text='Base currency'
    )
    alt_ccy = forms.ChoiceField(
        label='Alternate currency', choices=map(lambda r: (r, r), ccy.all()), help_text='Alternate currency'
    )

    class Meta:
        model = Trade
        fields = '__all__'

