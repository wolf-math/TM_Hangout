# utils.py

from calendar import HTMLCalendar
from datetime import datetime
from django.urls import reverse

class EventCalendar(HTMLCalendar):
    def __init__(self, events):
        super().__init__()
        self.events = self.group_by_day(events)

    def group_by_day(self, events):
        grouped_events = {}
        for event in events:
            day = event.event_date.day
            if day in grouped_events:
                grouped_events[day].append(event)
            else:
                grouped_events[day] = [event]
        return grouped_events

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if day in self.events:
                cssclass += ' filled'
                body = []
                for event in self.events[day]:
                    event_url = reverse('planner:event', args=[event.id])
                    event_time = event.event_date.strftime('%H:%M')
                    body.append(f'<li><a href="{event_url}">{event.name} ({event_time})</a></li>')
                return self.day_cell(cssclass, f'<span class="day">{day}</span> <ul> {"".join(body)} </ul>')
            return self.day_cell(cssclass, f'<span class="day">{day}</span>')
        return self.day_cell('noday', ' ')

    def day_cell(self, cssclass, body):
        return f'<td class="{cssclass}">{body}</td>'

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super().formatmonth(year, month)
