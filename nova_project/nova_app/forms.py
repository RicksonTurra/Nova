from django import forms
from .models import Events

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('name_field', 'tickets_field', 'date_field')
        
        class DateInput(forms.DateInput):
            input_type = 'date'

        widgets = {
            'date_field': DateInput(),
        }

        labels={
            "name_field": "Name",
            "tickets_field": "Tickets",
            "date_field": "Date"
        }