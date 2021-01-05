
from django import forms

# Local imports
from record_trades.models import Trade


class CreateNewTradeForm(forms.ModelForm):
    """
    ``Form``
        A boilerplate form created with :model:`record_trades.Trade` as the underlying model
    """

    class Meta:
        model = Trade
        fields = '__all__'

