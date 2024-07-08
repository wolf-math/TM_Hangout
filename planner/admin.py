from django.contrib import admin
from .models import Event, Attendance

# admin.site.register(Event)
admin.site.register(Attendance)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_date', 'manager')
    ordering = ('-event_date',)
    search_fields = ('name', 'event_date', 'manager')