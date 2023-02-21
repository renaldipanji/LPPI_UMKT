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

class JournalUmktForm(forms.ModelForm):
    class Meta:
        model = JournalUmktModel
        fields = ('judul_jurnal','issn','publication','index','deskripsi','cover_jurnal','link_view_jurnal','link_current_issue','link_online_submission','link_download_template','jenis_journal',)
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
                    'rows': '5',
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
            'jenis_journal' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                }
            ),
        }

type_file = [
('/static/landingpage/assets/img/logo/pdf.svg', 'PDF'),
('/static/landingpage/assets/img/logo/jpg.svg', 'JPG'),
('/static/landingpage/assets/img/logo/png.svg', 'PNG'),
]
class DownloadForm(forms.ModelForm):
    class Meta:
        model = DownloadContent
        fields = ['nama_file','jenis_file','ukuran_file','file_download']
        widgets = {
            'nama_file' : forms.TextInput(
                attrs={
                    'class':'form-control', 'placeholder':'Nama File'
                }),
            'jenis_file' : forms.Select(choices=type_file,
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
class FakultasForm(forms.ModelForm):
    class Meta:
        model = FakultasModel
        fields = ['nama_fakultas']
        widgets = {
            'nama_fakultas' : forms.TextInput(
                attrs={
                    'class':'form-control', 'placeholder':'Nama Fakultas'
                }), 
        }

class ProdiForm(forms.ModelForm):
    class Meta:
        model = ProdiModel
        fields = ['fakultas','nama_prodi']
        widgets = {
            'fakultas' : forms.Select(
            attrs={
                'class':'form-select'
            }),
            'nama_prodi' : forms.TextInput(
                attrs={
                    'class':'form-control', 'placeholder':'Nama Prodi'
                }), 
        }

class DosenForm(forms.ModelForm):
    class Meta:
        model = DosenModel
        fields = ['nidn','nama','prodi']
        widgets = {
            'nidn' : forms.TextInput(
                attrs={
                    'class':'form-control', 'placeholder':'NIDN'
            }), 
            'nama' : forms.TextInput(
                attrs={
                    'class':'form-control', 'placeholder':'Nama Dosen'
            }), 
            'prodi' : forms.Select(
            attrs={
                'class':'form-select'
            }),
        }

class MahasiswaForm(forms.ModelForm):
    class Meta:
        model = MahasiswaModel
        fields = ['nim','nama','angkatan','prodi']
        widgets = {
            'nim' : forms.TextInput(
                attrs={
                    'class':'form-control', 'placeholder':'NIM'
            }), 
            'nama' : forms.TextInput(
                attrs={
                    'class':'form-control', 'placeholder':'Nama Mahasiswa'
            }), 
            'angkatan' : forms.TextInput(
                attrs={
                    'class':'form-control', 'placeholder':'Angkatan'
            }), 
            'prodi' : forms.Select(
            attrs={
                'class':'form-select'
            }),
        }

class KategoriIndexForm(forms.ModelForm):
    class Meta:
        model = KategoriIndexModel
        fields = ['nama']
        widgets = {
            'nama' : forms.TextInput(
                attrs={
                    'class':'form-control', 'placeholder':'Nama Kategori Index'
            }),
        }
class PenelitianDosenForm(forms.ModelForm):
    class Meta:
        model = PenelitianDosenModel
        fields = ['judul','tahun','penyedia_jurnal','kategori_index','asal_pendanaan','total_pendanaan','link_publikasi','ketua_peneliti']
        widgets = {
            'judul' : forms.TextInput(
                attrs={
                    'class':'form-control', 'placeholder':'Judul Penelitian'
            }),
            'penyedia_jurnal' : forms.TextInput(
                attrs={
                    'class':'form-control', 'placeholder':'Penyedia Jurnal'
            }),
            'tahun' : forms.TextInput(
                attrs={
                    'class':'form-control yearpicker',
            }),
            'kategori_index' : forms.Select(
            attrs={
                'class':'form-select'
            }),
            'asal_pendanaan' : forms.TextInput(
                attrs={
                    'class':'form-control', 'placeholder':'Asal Pendanaan'
            }),
            'asal_pendanaan' : forms.TextInput(
                attrs={
                    'class':'form-control', 'placeholder':'Asal Pendanaan'
            }),
            'total_pendanaan' : forms.TextInput(
                attrs={
                    'class':'form-control'
            }),
            'link_publikasi' : forms.TextInput(
                attrs={
                    'class':'form-control', 'placeholder':'Link Publikasi'
            }),
            'ketua_peneliti' : forms.Select(
            attrs={
                'class':'form-select'
            }),
        }