from django import forms


class ConvertDevise(forms.Form):
    amount_to_convert = forms.FloatField()
    initial_unitee = forms.CharField(max_length=255)
    unitee_of_conversion = forms.CharField(max_length=255)
     