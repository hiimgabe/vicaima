# pylint: disable=missing-class-docstring
from django import forms
from .models import User, Event, Evaluation, Criteria, Colaborator

class AddEvent(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['begin_event', 'end_event', 'status', 'evaluated']
        widgets = {
            'begin_event': forms.DateTimeInput(attrs={'type': 'date', 'class': 'date-field'}),
            'end_event': forms.DateTimeInput(attrs={'type': 'date', 'class': 'date-field'}),
            # Add other fields' widgets if needed
        }

class	UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        
class	ColaboratorForm(forms.ModelForm):
    class Meta:
        model = Colaborator
        fields = ['fname','lname','username','department','role','admission_date','functional_group']

class DateInput(forms.DateInput):
    input_type = 'date'            
class	EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['begin_event','end_event','evaluated']
        widgets = {
            'begin_event': DateInput(),
            'end_event': DateInput(),
        }

class	EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['id_evaluator','id_evaluated','id_event','status']

class	CriteriaForm(forms.ModelForm):
    class Meta:
        model = Criteria
        fields = ['id_evaluation','question','answer','description','comment']
