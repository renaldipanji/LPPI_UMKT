from django import forms
from .models import *
from django.forms import widgets

class WorkprogrammeForm(forms.ModelForm):
    class Meta :
        model = Workprogramme
        fields = ('file_workprogramme',)
        widgets = {
            'file_workprogramme' : forms.FileInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'oninvalid': 'this.setCustomValidity("Data tidak boleh kosong")',
                    'oninput': 'setCustomValidity("")'
                }
            )
        }

# class VisimisiForm(forms.ModelForm):
#     class Meta :
#         model = Visimisi
#         fields = ('visi','misi',)
#         widgets = {
#             'visi' : forms.Text(
#                 attrs={
#                     'class':'form-control',
#                 }
#             )
#         }

class Journals(forms.ModelForm):
    class Meta :
        model = Journals
        fields = ('file_workprogramme',)
        widgets = {
            'file_workprogramme' : forms.FileInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'oninvalid': 'this.setCustomValidity("Data tidak boleh kosong")',
                    'oninput': 'setCustomValidity("")'
                }
            )
        }