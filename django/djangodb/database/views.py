from django.shortcuts import render
from .models import Colaborator, Event, Evaluation, Criteria

def	home(request):
	return render(request, 'home.html')

def	add_event(request):
	return render(request, 'add_event.html')
