from dataclasses import fields
from fileinput import FileInput
from django import forms
from .models import orgstruktur, sipena
from .models import divisippi
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

class SipenaForm(forms.ModelForm):
    class Meta:
        model = sipena
        fields = ('overview_sipena','flowservice_sipena',)
        widgets = {
            'overview_sipena' : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Overview',

                }
            ),
            'flowservice_sipena' : forms.FileInput(
                attrs={
                    'class': 'form-control form-control',
                    'oninvalid': 'this.setCustomValidity("Data tidak boleh kosong")',
                    'oninput': 'setCustomValidity("")',
                }
            ),
        }