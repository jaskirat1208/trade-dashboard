import ccy

from django import forms

# Local imports
from record_trades.models import Trade


class CreateNewTradeForm(forms.ModelForm):
    """
    ``Form``
        A boilerplate form created with :model:`record_trades.Trade` as the underlying model
    """
    trade_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'})
    )

    expiry_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'})
    )

    b_ccy = forms.ChoiceField(choices=map(lambda r: (r, r), ccy.all()))
    alt_ccy = forms.ChoiceField(choices=map(lambda r: (r, r), ccy.all()))

    class Meta:
        model = Trade
        fields = '__all__'

