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

class ArticletranslationForm(forms.ModelForm):
    class Meta:
        model = articletranslation
        fields = ('overview_articletranslation','flowservice_articletranslation')
        widgets = {
            'overview_articletranslation' : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Overview',

                }
            ),
            'flowservice_articletranslation' : forms.FileInput(
                attrs={
                    'class': 'form-control form-control',
                    'oninvalid': 'this.setCustomValidity("Data tidak boleh kosong")',
                    'oninput': 'setCustomValidity("")',
                }
            ),
        }