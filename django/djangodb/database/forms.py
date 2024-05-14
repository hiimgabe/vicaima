from django import forms
from .models import User, Event, Evaluation, Criteria, Colaborator

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

class	UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        
class	ColaboratorForm(forms.ModelForm):
	class Meta:
		model = Colaborator
		fields = ['fname','lname','username','department','role','admission_date','functional_group']
            
class	EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ['beginning','end','status']

class	EvaluationForm(forms.ModelForm):
	class Meta:
		model = Evaluation
		fields = ['id_evaluator','id_evaluated','id_event','status']

class	CriteriaForm(forms.ModelForm):
	class Meta:
		model = Criteria
		fields = ['id_evaluation','question','answer','description','comment']