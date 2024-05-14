from django import forms

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField()
    ab = forms.DateTimeField()
    ac = forms.DateField()
    ad = forms.DateField()
    a2 = forms.DateField()
