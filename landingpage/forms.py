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

class NewspaperForm(forms.ModelForm):
    class Meta:
        model = newspaper
        fields = ('nama_dosen','judul_artikel','tahun','link',)
        widgets = {
            'nama_dosen' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Nama Dosen',
                }
            ),
            'judul_artikel': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Judul Artikel',
                }
            ),
            'tahun': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Tahun',
                }
            ),
            'link': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Link',
                }
            )
        }
