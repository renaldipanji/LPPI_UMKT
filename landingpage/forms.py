from dataclasses import fields
from django import forms
from .models import *
from django.forms import widgets

class JournalServingForm(forms.ModelForm):
    class Meta:
        model = JournalServingModel
        fields = ('judul_jurnal','issn','publication','index','deskripsi','cover_jurnal','link_view_jurnal','link_current_issue','link_online_submission','link_download_template',)
        widgets = {
            'judul_jurnal' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Judul Jurnal',
                }
            ),
            'issn' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'ISSN',
                }
            ),
            'publication' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Publication',
                }
            ),
            'index' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'rows': '3',
                }
            ),
            'deskripsi' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'rows': '3',
                }
            ),
            'cover_jurnal' : forms.FileInput(
                attrs={
                    'class': 'form-control form-control',
                    'oninvalid': 'this.setCustomValidity("Data tidak boleh kosong")',
                    'oninput': 'setCustomValidity("")',
                }
            ),
            'link_view_jurnal' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Link View Jurnal',
                }
            ),
            'link_current_issue' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Link Current Issue',
                }
            ),
            'link_online_submission' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Link Online Submission',
                }
            ),
            'link_download_template' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Link Download Template',
                }
            ),
        }