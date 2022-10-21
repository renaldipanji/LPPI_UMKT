from dataclasses import fields
from django import forms
from .models import *
from django.forms import widgets

class OrgstrukturForm(forms.ModelForm):
    
    class Meta:
        model = OrgstrukturModel
        fields = ('orgstruktur_image',)
        widgets = {
            'orgstruktur_image': forms.FileInput(
                attrs= {
                    'class': 'form-control form-control',
                    'oninvalid': 'this.setCustomValidity("Data tidak boleh kosong")',
                    'oninput': 'setCustomValidity("")'
                }
            )
        }

class DivisippiForm(forms.ModelForm):

     class Meta:
         model = divisippi
         fields = ('overview_divisippi', 'flowservice_divisippi')
         widgets = {
             'overview_divisippi' : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Overview',

                }
            ),
            'flowservice_divisippi' : forms.FileInput(
                attrs={
                    'class': 'form-control form-control',
                    'oninvalid': 'this.setCustomValidity("Data tidak boleh kosong")',
                    'oninput': 'setCustomValidity("")',
                }
            ),
         }