from dataclasses import fields
from django import forms
from .models import *
from django.forms import widgets

class ElearningsupportForm(forms.ModelForm):
    class Meta:
        model = ElearningSupport
        fields = ('elearningsupport_overview','elearningsupport_flowservice',)
        widgets = {
            'elearningsupport_flowservice' : forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'oninvalid': 'this.setCustomValidity("Data tidak boleh kosong")',
                    'oninput': 'setCustomValidity("")',
                }
            ),
            'elearningsupport_overview' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'rows': '10',
                }
            ),
        }