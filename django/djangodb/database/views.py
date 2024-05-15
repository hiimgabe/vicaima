# pylint: disable=missing-class-docstring

from django.shortcuts import render, redirect
from .models import Colaborator, Event, Evaluation, Criteria
from .forms import AddEvent, UserForm, ColaboratorForm, EventForm, EvaluationForm, CriteriaForm
from django.shortcuts import get_object_or_404, redirect

def change_status(request, event_id):
    event = get_object_or_404(Event, id_event=event_id)
    event.status = True
    event.save()
    return redirect('show_events')

def	home(request):
    return render(request, 'home.html')

def dashboard(request):
    total_events = Event.objects.count()
    finished_events = Event.objects.filter(status=True).count()
    ongoing_events = total_events - finished_events

    context = {
        'total_events': total_events,
        'finished_events': finished_events,
        'ongoing_events': ongoing_events,
    }

    return render(request, 'dashboard.html', context)

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

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm()
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
