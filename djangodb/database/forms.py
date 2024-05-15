# pylint: disable=missing-class-docstring
from django import forms
from .models import User, Event, Evaluation, Criteria, Colaborator

class AddEvent(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['begin_event', 'end_event', 'type_of_evaluation', 'evaluator', 'evaluated']
        widgets = {
            'begin_event': forms.DateTimeInput(attrs={'type': 'date', 'class': 'date-field'}),
            'end_event': forms.DateTimeInput(attrs={'type': 'date', 'class': 'date-field'}),
        }

class	UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        
class	ColaboratorForm(forms.ModelForm):
    class Meta:
        model = Colaborator
        fields = ['fname','lname','department','role','admission_date','functional_group']

class DateInput(forms.DateInput):
    input_type = 'date'            

class	EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['id_evaluator','id_evaluated','id_event','status']

class	CriteriaForm(forms.ModelForm):
    class Meta:
        model = Criteria
        fields = ['id_evaluation','question','answer','description','comment']

class UploadCSVForm(forms.Form):
	csv_file = forms.FileField()