from django import forms
from django.forms import ModelForm
from .models import Event

class EventForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter event name'
        }),
        label=''
    )
    event_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control',
            'placeholder': 'Select a date and time'
        }),
        label=''
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter event description',
            'rows': 4
        }),
        required=False,
        label=''
    )
    location = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter event location'
        }),
        label=''
    )
    # multi_person = forms.BooleanField(
    #     widget=forms.CheckboxInput(attrs={
    #         'class': 'form-check-input',
    #         'id': 'multi_perosn'
    #     }),
    #     required=False,
    #     label="Limit number of attendees?",
    # )
    max_attendees = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter maximum number of attendees'
        }),
        label='Max attendees (if space is limited)',
        required=False
    )

    class Meta:
        model = Event
        fields = ['name', 'event_date', 'description', 'location', 'multi_person', 'max_attendees']

    def clean(self):
        cleaned_data = super().clean()
        multi_person = cleaned_data.get('multi_person')
        max_attendees = cleaned_data.get('max_attendees')

        if multi_person and not max_attendees:
            self.add_error('max_attendees', 'This field is required if multi-person is checked.')

        return cleaned_data
