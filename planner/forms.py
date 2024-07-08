from django import forms
from django.forms import ModelForm
from .models import Event

class EventForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter event name'
        }),
        label='Event Name'
    )
    event_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control',
            'placeholder': 'Select a date and time'
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter event description',
            'rows': 4
        }),
        required=False
    )
    location = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter event location'
        })
    )
    multi_person = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        }),
        required=False
    )
    max_attendees = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter maximum number of attendees'
        })
    )

    class Meta:
        model = Event
        fields = ['name', 'event_date', 'description', 'location', 'multi_person', 'max_attendees']
