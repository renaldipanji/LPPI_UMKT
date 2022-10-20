from django import forms
from .models import *
from django.forms import widgets

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