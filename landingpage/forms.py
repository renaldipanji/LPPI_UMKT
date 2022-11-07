from django import forms
from .models import *
from django.forms import widgets

CHOICES = [('False', 'Belum'), ('True', 'Sudah')]

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
        fields = ('nidn','nama_dosen','program_studi','fakultas','judul_artikel','tahun','link')
        widgets = {
            'nidn' : forms.TextInput (
                attrs={
                    'class':'form-control',
                    'placeholder' : 'NIDN',
                }
            ),
            'nama_dosen' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder' : 'Nama Dosen',
                }
            ),
            'program_studi' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder' : 'Program Studi',
                }
            ),
            'fakultas' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder' : 'Fakultas',
                }
            ),
            'judul_artikel' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder' : 'Judul Artikel',
                }
            ),
            'tahun' : forms.TextInput(
                attrs={
                    'class':'form-control yearpicker',
                    'placeholder' : 'Tahun',
                }
            ),
            'link' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder' : 'Link',
                }
            ),
        }
        
class TextBookForm(forms.ModelForm):
    class Meta:
        model = TextBooksModel
        fields = ('nidn','nama_dosen','program_studi','fakultas','judul_buku','tahap_luaran_10','tahap_luaran_40','tahap_luaran_80','reviewer','tahun','link')
        widgets = {
            'nidn' : forms.TextInput (
                attrs={
                    'class':'form-control',
                    'placeholder' : 'NIDN',
                }
            ),
            'nama_dosen' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder' : 'Nama Dosen',
                }
            ),
            'program_studi' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder' : 'Program Studi',
                }
            ),
            'fakultas' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder' : 'Fakultas',
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
                     'class':'yearpicker form-control',
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
        
class EventForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = ('event_image',)
        widgets = {
            'event_image': forms.FileInput(
                attrs = {
                    'class': 'form-control', 
                    'oninvalid': 'this.setCustomValidity("Data tidak boleh kosong")',
                    'oninput': 'setCustomValidity("")',   
                }
            ),
        }
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('no_hp', 'email', 'ig', 'alamat',)
        widgets = {
            'no_hp' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'No Handphone',
                }
            ),
            
            'email' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Email',
                }
            ),
            
            'ig' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Instagram',
                }
            ),
            
            'alamat' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'rows'  : '3',
                    'placeholder' : 'Alamat',
                }
            ),
        }

class DivisiForm(forms.ModelForm):

     class Meta:
         model = DivisiModel
         fields = ('overview_divisi', 'members_divisi')
         widgets = {
             'overview_divisi' : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Overview',

                }
            ),
            'members_divisi' : forms.FileInput(
                attrs={
                    'class': 'form-control form-control',
                    'oninvalid': 'this.setCustomValidity("Data tidak boleh kosong")',
                    'oninput': 'setCustomValidity("")',
                }
            ),
         }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceModel
        fields = ('overview_service','flowservice_service')
        widgets = {
            'overview_service' : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Overview',

                }
            ),
            'flowservice_service' : forms.FileInput(
                attrs={
                    'class': 'form-control form-control',
                    'oninvalid': 'this.setCustomValidity("Data tidak boleh kosong")',
                    'oninput': 'setCustomValidity("")',
                }
            ),
        }