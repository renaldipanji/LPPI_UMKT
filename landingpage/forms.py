from dataclasses import fields
from django import forms
from .models import orgstruktur
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