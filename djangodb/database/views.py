from django.shortcuts import render, redirect
from .models import Colaborator, Event, Evaluation, Criteria
from .forms import RenewBookForm, UserForm, ColaboratorForm, EventForm, EvaluationForm, CriteriaForm


def	home(request):
	return render(request, 'home.html')

def	add_event(request):
	return render(request, 'add_event.html')

def	add_user(request):
	return render(request, 'add_user.html')

def add_event(request):
    form = RenewBookForm()
    return render(request, 'add_event.html', {'form': form})

def aval_form(request):
	return render(request, 'aval_form.html', {})

def aval_list(request):
	return render(request, 'aval_list.html', {})

def add_user(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		colaborator_form = ColaboratorForm(request.POST)
		if user_form.is_valid() and colaborator_form.is_valid():
			user_form.save()
			colaborator_form.save()
			return redirect('home')
		else:
			user_form = UserForm()
			colaborator_form = ColaboratorForm()

		context = {
			'user_form': user_form,
			'colaborator_form': colaborator_form
		}
		return render(request, 'add_user.html', context)
