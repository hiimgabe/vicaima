from django.shortcuts import render
from .models import Colaborator, Event, Evaluation, Criteria

def	home(request):
	all_users = Colaborator.objects.all
	return render(request, 'home.html', {'all':all_users})