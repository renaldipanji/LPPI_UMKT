from django import forms
from .models import Workprogramme
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