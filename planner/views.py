from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event
from .forms import EventForm
from django.http import HttpResponseRedirect, HttpResponseForbidden

@login_required
def planner(request):
    now = datetime.now()
    year = now.year
    month_number = now.month
    
    cal = HTMLCalendar(calendar.SUNDAY).formatmonth(year, month_number)

    return render(request, 'planner.html', {
        "name": request.user,
        "year": year,
        "month": month,
        "cal": cal
    })

@login_required
def month(request, year = None, month = None):
    print("YEAR", year)
    print("MONTH", month)
    if year is None:
        year = datetime.now().year
    if month is None:
        month = datetime.now().strftime('%B')

    # Convert month from name to number
    month_number = list(calendar.month_name).index(month.title()) 
    month_number = int(month_number)

    # Create calendar
    cal = HTMLCalendar(calendar.SUNDAY).formatmonth(year, month_number)

    return render(request, 'planner.html', {
        "name": request.user,
        "year": year,
        "month": month,
        "cal": cal
    })

@login_required
def all_events(request):
    event_list = Event.objects.all().order_by('-event_date')
    return render(request, 'events.html', {'event_list': event_list})

@login_required
def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.manager = request.user
            event.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_event.html', {'form': form, 'submitted': submitted})

@login_required
def event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    # if event.user != request.user:
    #     return HttpResponseForbidden("You are not authorized to view this event.")

    return render(request, 'event.html', {'event': event, 'user': request.user.id })