from django import forms
from .models import rideRequest


class FlightForm(forms.ModelForm):
        start_name = forms.CharField(widget=forms.HiddenInput())
        end_name = forms.CharField(widget=forms.HiddenInput())
        start_lng = forms.FloatField(widget=forms.HiddenInput())
        start_lat = forms.FloatField(widget=forms.HiddenInput())
        end_lng = forms.FloatField(widget=forms.HiddenInput())
        end_lat = forms.FloatField(widget=forms.HiddenInput())

        class Meta:
            model = rideRequest
            fields = ['start_name', 'end_name', 'start_lng', 'start_lat', 'end_lng', 'end_lat']
    
        def clean(self):
            cleaned_data = super().clean()
            return cleaned_data