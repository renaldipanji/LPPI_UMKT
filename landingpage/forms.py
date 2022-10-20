from dataclasses import fields
from django import forms
from .models import *
from django.forms import widgets

class UmktPressForm(forms.ModelForm):
    class Meta:
        model = UmktPress
        fields = ('umktpress_overview','umktpress_flowservice',)
        widgets = {
            'umktpress_flowservice' : forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'oninvalid': 'this.setCustomValidity("Data tidak boleh kosong")',
                    'oninput': 'setCustomValidity("")',
                }
            ),
            'umktpress_overview' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'rows': '10',
                }
            ),
        }