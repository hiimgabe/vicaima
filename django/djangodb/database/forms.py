from django import forms

class RenewBookForm(forms.Form):
    EVALUATOR_CHOICES = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
    ]
    Begin_Date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'date-field'}))
    End_Date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'date-field'}))
    Evaluator = forms.ChoiceField(choices=EVALUATOR_CHOICES, widget=forms.Select(), required=True)
    ad = forms.DateField()
    a2 = forms.DateField()
