from django import forms
from .models import User, Event, Evaluation, Criteria, Colaborator

class	RenewBookForm(forms.Form):
    renewal_date = forms.DateField()
    ab = forms.DateTimeField()
    ac = forms.DateField()
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