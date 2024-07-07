from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import calendar
from calendar import HTMLCalendar
from datetime import datetime

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
