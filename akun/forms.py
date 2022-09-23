from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import widgets

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "input100"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input100"
            }
        )
    )

class ForgetPassForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "input100"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input100"
            }
        )
    )

class ProfilForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ('email', 'nama', 'nama_institusi','no_hp')
        widgets = {
                'email' : forms.TextInput(attrs={
                    'class':'form-control'
                }),
                'nama' : forms.TextInput(attrs={
                    'class':'form-control'
                }),
                'no_hp' : forms.TextInput(attrs={
                    'class':'form-control'
                }),
                'nama_institusi' : forms.TextInput(attrs={
                    'class':'form-control'
                }),
        }
        def __init__(self, *args, **kwargs):
            super(ProfilForm, self).__init__(*args, **kwargs)
            self.fields['nama'].required = False

class ResetPassForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ('email', 'nama', 'nama_institusi','no_hp')
        widgets = {
                'email' : forms.TextInput(attrs={
                    'class':'form-control'
                }),
                'nama' : forms.TextInput(attrs={
                    'class':'form-control'
                }),
                'no_hp' : forms.TextInput(attrs={
                    'class':'form-control'
                }),
                'nama_institusi' : forms.TextInput(attrs={
                    'class':'form-control'
                }),
        }
        def __init__(self, *args, **kwargs):
            super(ProfilForm, self).__init__(*args, **kwargs)
            self.fields['nama'].required = False

class ProfilFotoForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ('foto_profile',)
        widgets = {
            'foto_profile': forms.FileInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'oninvalid': 'this.setCustomValidity("Data tidak boleh kosong")',
                    'oninput': 'setCustomValidity("")'
                }
            ),    
        }

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': False})
    class Meta:
        # jenis institusi
        pil_institusi = (
        ('0','Umum'),
        ('1','Mahasiswa UMKT'),
        ('2','Dosen / Staff UMKT'),
        )        
        model = User
        fields = ('email', 'is_active' , 'username' , 'password1', 'institusi', 'nama','no_hp', 'password2')

        widgets = {
            'email' : forms.TextInput(attrs={
                'class':'input100 email'
            }),
            'is_active' : forms.HiddenInput(attrs={
                'value': '0'
            }),
            'nama' : forms.TextInput(attrs={
                'class':'input100', 'value':'-', 'hidden':'hidden'
            }),
            'username' : forms.TextInput(attrs={
                'class':'input100'
            }),
            'no_hp' : forms.TextInput(attrs={
                'class':'input100'
            }),
            'institusi' : forms.Select(choices=pil_institusi,attrs={
                'class':'form-select', 'style':'width: 48%; font-size: 16px; background-color: #f7f7f7;color: #555555;'
            }),
            'password1' : forms.PasswordInput(attrs={
                'class':'input100'
            }),
            'password2' : forms.PasswordInput(attrs={
                'class':'input100'
            }),
        }
