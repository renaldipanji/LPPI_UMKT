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
        model = NewspaperModel
        fields = ('nidn','nama_dosen','program_studi','fakultas','judul_artikel','tahun','link',)
        widgets = {
            'nidn' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'NIDN',
                }
            ),
            'nama_dosen' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Nama Dosen',
                }
            ),
            'program_studi' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Program Studi',
                }
            ),
            'fakultas' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Fakultas',
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
