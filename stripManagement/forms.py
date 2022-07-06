from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import TextInput, NumberInput, TimeInput, DateInput

from .models import *


class FlightForm(forms.ModelForm):
    class Meta:
        model = flightPlan
        fields = (
        'aircraft_id', 'flight_num', 'company', 'departAirport', 'destAirport', 'safety_airport', 'estDepTime',
        'estArrTime', 'flight_level', 'flight_speed', 'transpondeur', 'board_equipment', 'turbulance', 'flight_type',
        'flight_route', 'totPassengers', 'dateFrom', 'dateTo')
        widgets ={
            'aircraft_id': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 1100px;',
                'placeholder': 'aircraft id'
            }),
            'flight_num': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 1100px;',
                'placeholder': 'flight number'
            }),

            'departAirport': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 1100px;',
                'placeholder': 'departure airport'
            }),
            'destAirport': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 1100px;',
                'placeholder': 'destination airport'
            }),
            'safety_airport': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 1100px;',
                'placeholder': 'safety airport'
            }),
            'estDepTime': TimePickerInput(attrs={
                'class': "form-control",
                'style': 'max-width: 1100px;',
                'placeholder': 'estimated departure time'
            }),
            'estArrTime': TimePickerInput(attrs={
                'class': "form-control",
                'style': 'max-width: 1100px;',
                'placeholder': 'estimated arrival time'
            }),
            'flight_level': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 1100px;',
                'placeholder': 'flight level'
            }),
            'flight_route': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 1100px;',
                'placeholder': 'flight route, seperate routes by commas'
            }),

            'flight_speed': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 1100px;',
                'placeholder': 'Flight speed'
            }),

            'flight_type': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 1100px;',
                'placeholder': 'Flight type'
            }),

            'transpondeur': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 1100px;',
                'placeholder': 'Transpondeur'
            }),

            'board_equipment': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 1100px;',
                'placeholder': 'Board Equipment'
            }),

            'turbulance': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 1100px;',
                'placeholder': 'turbulance'
            }),

            'totPassengers': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 1100px;',
                'placeholder': 'total passengers'
            }),
            'dateFrom': DatePickerInput(attrs={
                'class': "form-control",
                'style': 'max-width: 1100px;',
                'placeholder': 'date from'
            }),
            'dateTo': DatePickerInput(attrs={
                'class': "form-control",
                'style': 'max-width: 1100px;',
                'placeholder': 'date to'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save flight plan', css_class="btn btn-success col-md-12"))