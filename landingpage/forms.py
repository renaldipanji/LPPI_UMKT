from django import forms
from .models import *
from django.forms import widgets

CHOICES = [('False', 'False'), ('True', 'True')]

class OrgstrukturForm(forms.ModelForm):
    class Meta :
        model = OrgstrukturModel
        fields = ('orgstruktur_image',)
        widgets = {
            'orgstruktur_image' : forms.FileInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'oninvalid': 'this.setCustomValidity("Data tidak boleh kosong")',
                    'oninput': 'setCustomValidity("")'
                }
            )
        }
class WorkProgrammeForm(forms.ModelForm):
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

class VisiMisiForm(forms.ModelForm):
    class Meta :
        model = VisiMisiModel
        fields = ('visi','misi',)
        widgets = {
            'visi' : forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder' : 'Visi',
                }
            ),
            'misi' : forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder' : 'Misi',
                }
            ),
        }

class JournalsForm(forms.ModelForm):
    class Meta :
        model = JournalsModel
        fields = ('nama','judul_artikel','tahun','link')
        widgets = {
            'nama' : forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder' : 'Nama',
                }
            ),
            'judul_artikel' : forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder' : 'Judul Artikel',
                }
            ),
            'tahun' : forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder' : 'Tahun',
                }
            ),
            'link' : forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder' : 'Link',
                }
            ),
        }
        
class TextBookForm(forms.ModelForm):
    class Meta:
        model = TextBooksModel
        fields = ('program_studi','nama','judul_buku','tahap_luaran_10','tahap_luaran_40','tahap_luaran_80','reviewer','tahun','link')
        widgets = {
            'program_studi' : forms.TextInput(
                 attrs={
                     'class':'form-control',
                     'placeholder' : 'Program Studi',
                 }
            ),
            'nama' : forms.TextInput(
                 attrs={
                     'class':'form-control',
                     'placeholder' : 'Nama'
                }
            ),
            'judul_buku' : forms.TextInput(
                 attrs={
                     'class':'form-control',
                     'placeholder' : 'Judul Buku'
                }
            ),
            'tahap_luaran_10' : forms.Select(choices=CHOICES,
                 attrs={
                     'class':'form-control',
                     'placeholder' : 'Tahap Luaran 10'
                }
            ),
            'tahap_luaran_40' : forms.Select(choices=CHOICES,
                 attrs={
                     'class':'form-control',
                     'placeholder' : 'Tahap Luaran 40'
                }
            ),
            'tahap_luaran_80' : forms.Select(choices=CHOICES,
                 attrs={
                     'class':'form-control',
                     'placeholder' : 'Tahap Luaran 80'
                }
            ),
            'reviewer' : forms.TextInput(
                 attrs={
                     'class':'form-control',
                     'placeholder' : 'Reviewer'
                }
            ),
            'tahun' : forms.TextInput(
                 attrs={
                     'class':'form-control',
                     'placeholder' : 'Tahun'
                }
            ),
            'link' : forms.TextInput(
                 attrs={
                     'class':'form-control',
                     'placeholder' : 'Link'
                }
            ),
        }
        
