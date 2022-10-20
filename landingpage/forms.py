from dataclasses import fields
from django import forms
from .models import *
from django.forms import widgets

class OrgstrukturForm(forms.ModelForm):
    
    class Meta:
        model = orgstruktur
        fields = ('file_orgstruktur',)
        widgets = {
            'file_orgstruktur': forms.FileInput(
                attrs={
                    'class': 'form-control form-control',
                    'oninvalid': 'this.setCustomValidity("Data tidak boleh kosong")',
                    'oninput': 'setCustomValidity("")'
                }
            )
        }

class DivisielearningForm(forms.ModelForm):
    class Meta:
        model = divisielearning
        fields = ('overview_divisielearning','flowservice_divisielearning')
        widgets = {
            'overview_divisielearning' : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Overview',

                }
            ),
            'flowservice_divisielearning' : forms.FileInput(
                attrs={
                    'class': 'form-control form-control',
                    'oninvalid': 'this.setCustomValidity("Data tidak boleh kosong")',
                    'oninput': 'setCustomValidity("")',
                }
            ),
        }

