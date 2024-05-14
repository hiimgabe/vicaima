from django.shortcuts import render
from .models import Colaborator, Event, Evaluation, Criteria
from .forms import RenewBookForm


def	home(request):
	return render(request, 'home.html')

def	add_event(request):
	return render(request, 'add_event.html')

def	add_user(request):
	return render(request, 'add_user.html')

def add_event(request):
    form = RenewBookForm()
    return render(request, 'add_event.html', {'form': form})