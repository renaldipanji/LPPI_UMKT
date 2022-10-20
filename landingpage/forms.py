from django import forms
from .models import *
from django.forms import widgets

class EventForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = ('event_image',)
        widgets = {
            'event_image': forms.FileInput(
                attrs = {
                    'class': 'form-control', 
                    'oninvalid': 'this.setCustomValidity("Data tidak boleh kosong")',
                    'oninput': 'setCustomValidity("")',   
                }
            ),
        }