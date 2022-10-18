from dataclasses import fields
from django import forms
from .models import orgstruktur
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

# class DivisippiForm(forms.ModelForm):

#     class Meta:
#         model = divisippi
#         fields = ('file_divisippi',)
#         widgets = {
#             'file_divisippi': forms.FileInput(
#                 attrs={
#                     'class': 'form-control form-control',
#                     'oninvalid': 'this.setCustomValidity("Data tidak boleh kosong")',
#                     'oninput': 'setCustomValidity("")'
#                 }
#             )
#         }