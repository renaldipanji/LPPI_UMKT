from django import forms
from .models import *
from django.forms import widgets

class WorkprogrammeForm(forms.ModelForm):
    class Meta :
        model = WorkProgrammeModel
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