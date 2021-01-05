from django import forms
from record_trades.models import Trade


class CreateNewTradeForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Trade
        exclude = ()

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

