from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event
from .forms import EventForm
# from django.http import HttpResponseRedirect, HttpResponseForbidden
from .utils import EventCalendar
from datetime import datetime, timedelta


@login_required
def planner(request, year=None, month=None):
    if year is None or month is None:
        now = datetime.now()
        year = now.year
        month = now.month
    else:
        month_number = list(calendar.month_name).index(month.title())
        year = int(year)
        month = month_number

    # Calculate previous and next month
    first_day = datetime(year, month, 1)
    last_month = (first_day - timedelta(days=1)).replace(day=1)
    next_month = (first_day + timedelta(days=32)).replace(day=1)
    
    # Get events for the specified month
    events = Event.objects.filter(event_date__year=year, event_date__month=month)

    # Create calendar
    cal = EventCalendar(events).formatmonth(year, month)

    return render(request, 'planner.html', {
        "name": request.user,
        "year": year,
        "month": calendar.month_name[month],
        "cal": cal,
        "prev_year": last_month.year,
        "prev_month": last_month.strftime('%B'),
        "next_year": next_month.year,
        "next_month": next_month.strftime('%B')
    })

@login_required
def month(request, year=None, month=None):
    if year is None or month is None:
        now = datetime.now()
        year = now.year
        month = now.month
    else:
        month_number = list(calendar.month_name).index(month.title())
        year = int(year)
        month = month_number

    # Calculate previous and next month
    first_day = datetime(year, month, 1)
    last_month = (first_day - timedelta(days=1)).replace(day=1)
    next_month = (first_day + timedelta(days=32)).replace(day=1)
    
    # Get events for the specified month
    events = Event.objects.filter(event_date__year=year, event_date__month=month)

    # Create calendar
    cal = EventCalendar(events).formatmonth(year, month)

    return render(request, 'planner.html', {
        "name": request.user,
        "year": year,
        "month": calendar.month_name[month],
        "cal": cal,
        "prev_year": last_month.year,
        "prev_month": last_month.strftime('%B'),
        "next_year": next_month.year,
        "next_month": next_month.strftime('%B')
    })

@login_required
def all_events(request):
    event_list = Event.objects.all().order_by('-event_date')
    return render(request, 'events.html', {'event_list': event_list})

@login_required
def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.manager = request.user
            event.save()
            
            return redirect('planner:event', event_id=event.id) 
    form = EventForm        
    return render(request, 'add_event.html', {'form': form})

@login_required
def event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    return render(request, 'event.html', {'event': event, 'user': request.user.id })


@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('planner:event', event_id=event.id) 
    
    return render(request, 'edit_event.html', {'event': event, 'user': request.user.id, 'form': form })

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.user == event.manager:
        event.delete()
        messages.success(request, ("Event Deleted"))
    else:
        messages.success(request, ("You can't do that"))
    
    return redirect('planner:all_events') 