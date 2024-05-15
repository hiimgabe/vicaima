from django.shortcuts import render, redirect
from .models import Colaborator, Event, Evaluation, Criteria
from .forms import AddEvent, UserForm, ColaboratorForm, EventForm, EvaluationForm, CriteriaForm
from django.shortcuts import get_object_or_404, redirect


def	home(request):
	return render(request, 'home.html')

def add_event(request):
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