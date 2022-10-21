from django import forms
from .models import *
from django.forms import widgets

class DownloadForm(forms.ModelForm):
    class Meta:
        model = DownloadContent
        fields = ['nama_file','jenis_file','ukuran_file','file_download']
        widgets = {
            'nama_file' : forms.TextInput(
                attrs={
                    'class':'form-control', 'placeholder':'Nama File'
                }),
            'jenis_file' : forms.TextInput(
                attrs={
                    'class':'form-control', 'placeholder':'Jenis File'
                }),
            'ukuran_file' : forms.TextInput(
                attrs={
                    'class':'form-control', 'placeholder':'Ukuran File'
                }),
            'file_download': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'oninvalid': 'this.setCustomValidity("Data tidak boleh kosong")',
                    'oninput': 'setCustomValidity("")'
                }
            ), 
        }