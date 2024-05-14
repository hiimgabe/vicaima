from django import forms

class RenewBookForm(forms.Form):
    Begin_Date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    End_Date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    ac = forms.DateField()
    ad = forms.DateField()
    a2 = forms.DateField()
