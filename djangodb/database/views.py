from django.shortcuts import render, redirect, get_object_or_404
from .models import Colaborator, Event, Evaluation
from .forms import AddEvent, UserForm, ColaboratorForm, UploadCSVForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from datetime import datetime
import csv
import io

def	home(request):
    return render(request, 'home.html')

def add_event(request):
    if request.method == 'POST':
        form = AddEvent(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event was successfully added.')
            return redirect('add_event')
    else:
        form = AddEvent()

    return render(request, 'add_event.html', {'form': form})

def eval_form(request):
	return render(request, 'eval_form.html', {})

def evaluated_form(request):
	return render(request, 'evaluated_form.html', {})

def eval_list(request):
	evaluations = Evaluation.objects.filter(id_event=1)
	return render(request, 'eval_list.html', {'evals':evaluations})

def add_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        colaborator_form = ColaboratorForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
        if colaborator_form.is_valid():
            colaborator = colaborator_form.save(commit=False)
            colaborator.id_colaborator = user
            colaborator.save()
            return redirect('home')
    user_form = UserForm()
    colaborator_form = ColaboratorForm()
    context = {
        'user_form': user_form,
        'colaborator_form': colaborator_form
    }
    return render(request, 'add_user.html', context)

def add_user_csv(request):
	if request.method == 'POST':
		form = UploadCSVForm(request.POST, request.FILES)
		if form.is_valid():
			csv_file = request.FILES['csv_file']
			data_set = csv_file.read().decode('ISO-8859-1')
			io_string = io.StringIO(data_set)
			next(io_string)
			for column in csv.reader(io_string, delimiter=';', quotechar="|"):
				try:
					if len(column) < 9:  # Check if there are enough columns
						print(f"Skipping row due to insufficient columns: {column}")
						continue

					admission_date = column[6]
					try:
						parsed_date = datetime.strptime(admission_date, '%d/%m/%Y')
					except ValueError:
						print(f"Skipping row due to invalid date: {admission_date}")
						continue

					user, created = User.objects.get_or_create(
						username=column[1],
						defaults={'password': make_password('default_password')}
					)
					if created:
						user.save()

					colaborator, created = Colaborator.objects.get_or_create(
						id_colaborator=user,
						defaults={
							'num_colaborator': column[0],
							'fname': column[1],
							'lname': column[2],
							'department': column[4],
							'role': column[5],
							'admission_date': parsed_date,
							'functional_group': column[7]
						}
					)
					if created:
						colaborator.save()
				except Exception as e:
					print(f"Error: {e}")
	else:
		form = UploadCSVForm()
	return render(request, 'add_user_csv.html', {'form': form})

def dashboard(request):
    total_events = Event.objects.count()
    finished_events = Event.objects.filter(status=True).count()
    ongoing_events = total_events - finished_events

    context = {
        'total_events': total_events,
        'finished_events': finished_events,
        'ongoing_events': ongoing_events,
    }

def change_status(request, event_id):
    event = get_object_or_404(Event, id_event=event_id)
    event.status = True
    event.save()
    return redirect('show_events')

def show_events(request):
    status = request.GET.get('status', 'all')

    if status == 'all':
        events = Event.objects.all()
    elif status == 'true':
        events = Event.objects.filter(status=True)
    elif status == 'false':
        events = Event.objects.filter(status=False)
    else:
        events = Event.objects.all()  # Fallback to showing all events

    return render(request, 'show_events.html', {'events': events})