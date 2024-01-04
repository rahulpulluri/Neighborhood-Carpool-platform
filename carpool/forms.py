# forms.py

from django import forms
from .models import CarPool

class CarpoolForm(forms.ModelForm):
    class Meta:
        model = CarPool
        fields = ['carModel', 'departureTime', 'arrivalTime', 'route', 'availableSeats']
