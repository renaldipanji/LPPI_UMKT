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
class AnggotaPenelitiDosenForm(forms.ModelForm):
    class Meta:
        model = AnggotaPenelitiDosenModel
        fields = ['anggota_dosen']
        widgets = {
            'anggota_dosen' : forms.Select(
            attrs={
                'class':'form-select chosen-select'
            }),
        }
class AnggotaPenelitiMahasiswaForm(forms.ModelForm):
    class Meta:
        model = AnggotaPenelitiMahasiswaModel
        fields = ['anggota_mahasiswa']
        widgets = {
            'anggota_mahasiswa' : forms.Select(
            attrs={
                'class':'form-select chosen-select'
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

class PengabdianDosenForm(forms.ModelForm):
    class Meta:
        model = PengabdianDosenModel
        fields = ['judul','tahun','asal_pendanaan','total_pendanaan','link_laporan','ketua_peneliti']
        widgets = {
            'judul' : forms.TextInput(
                attrs={
                    'class':'form-control', 'placeholder':'Judul Pengabdian'
            }),
            'tahun' : forms.TextInput(
                attrs={
                    'class':'form-control yearpicker',
            }),
            'asal_pendanaan' : forms.TextInput(
                attrs={
                    'class':'form-control', 'placeholder':'Asal Pendanaan'
            }),
            'total_pendanaan' : forms.TextInput(
                attrs={
                    'class':'form-control'
            }),
            'link_laporan' : forms.TextInput(
                attrs={
                    'class':'form-control', 'placeholder':'Link Laporan'
            }),
            'ketua_peneliti' : forms.Select(
            attrs={
                'class':'form-select'
            }),
        }
class AnggotaPengabdianDosenForm(forms.ModelForm):
    class Meta:
        model = AnggotaPengabdianDosenModel
        fields = ['anggota_dosen']
        widgets = {
            'anggota_dosen' : forms.Select(
            attrs={
                'class':'form-select chosen-select'
            }),
        }
class AnggotaPengabdianMahasiswaForm(forms.ModelForm):
    class Meta:
        model = AnggotaPengabdianMahasiswaModel
        fields = ['anggota_mahasiswa']
        widgets = {
            'anggota_mahasiswa' : forms.Select(
            attrs={
                'class':'form-select chosen-select'
            }),
        }
class TeamTeachingForm(forms.ModelForm):
    class Meta:
        model = TeamTeachingModel
        fields = ['team_teaching']
        widgets = {
            'team_teaching' : forms.Select(
            attrs={
                'class':'form-select chosen-select'
            }),
        }
class matkulForm(forms.ModelForm):
    class Meta:
        list_prodi =(
        ("TI","Teknik Informatika"),
        ("TS","Teknik Sipil"),
        ("TM","Teknik Mesin"),
        ("Farmasi","Farmasi"),
        ("Kesmas","Kesehatan Masyarakat"),
        ("KepS1","Keperawatan S1"),
        ("KepD3","Keperawatan D3"),
        ("KeslingS1","Kesehatan Lingkungan S1"),
        ("KeslingD3","Kesehatan Lingkungan D3"),
        ("PBI","Pendidikan Bahasa Inggris"),
        ("POR","Pendidikan Olahraga"),
        ("HI","Hubungan Internasional"),
        ("Psikologi","Psikologi"),
        ("Hukum","Hukum"),
        ("Manajemen","Manajemen"),
        ("Lainnya","Lainnya"),
    )
        model = ValidasiOpl
        fields = ['kode_matkul', 'nama_matkul','prodi','link_matkul','pemilik_course']

        widgets = {
            'kode_matkul' : forms.TextInput(attrs={
                'class':'form-control'
            }),
            'nama_matkul': forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'link_matkul': forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'prodi': forms.Select(choices = list_prodi,attrs={
                'class' : 'form-select'
            }),
            'pemilik_course': forms.Select(attrs={
                'class' : 'form-control'
            }),
        }



class validasiOplForm(forms.ModelForm):
    class Meta:
        # status HAKI Course
        pil_status_haki = (
        ('0','Belum'),
        ('1','Dalam Pengajuan'),
        ('2','Sudah'),
        )        
        model = ValidasiOpl
        fields = ['ch1', 'ch2','ch3','ch4','ch5','ch6','ch7','ch8','ch9','ch10','ch11','ch12','ch13','ch14','keterangan','status_haki','progres']

        widgets = {
            'ch1' : forms.NumberInput(attrs={
            'class':'form-control', 'step':'0.1', 'min':'0', 'max':'1'
            }),
            'ch2' : forms.NumberInput(attrs={
            'class':'form-control', 'step':'0.1', 'min':'0', 'max':'1'
            }),
            'ch3' : forms.NumberInput(attrs={
            'class':'form-control', 'step':'0.1', 'min':'0', 'max':'1'
            }),
            'ch4' : forms.NumberInput(attrs={
            'class':'form-control', 'step':'0.1', 'min':'0', 'max':'1'
            }),
            'ch5' : forms.NumberInput(attrs={
            'class':'form-control', 'step':'0.1', 'min':'0', 'max':'1'
            }),
            'ch6' : forms.NumberInput(attrs={
            'class':'form-control', 'step':'0.1', 'min':'0', 'max':'1'
            }),
            'ch7' : forms.NumberInput(attrs={
            'class':'form-control', 'step':'0.1', 'min':'0', 'max':'1'
            }),
            'ch8' : forms.NumberInput(attrs={
            'class':'form-control', 'step':'0.1', 'min':'0', 'max':'1'
            }),
            'ch9' : forms.NumberInput(attrs={
            'class':'form-control', 'step':'0.1', 'min':'0', 'max':'1'
            }),
            'ch10' : forms.NumberInput(attrs={
            'class':'form-control', 'step':'0.1', 'min':'0', 'max':'1'
            }),
            'ch11' : forms.NumberInput(attrs={
            'class':'form-control', 'step':'0.1', 'min':'0', 'max':'1'
            }),
            'ch12' : forms.NumberInput(attrs={
            'class':'form-control', 'step':'0.1', 'min':'0', 'max':'1'
            }),
            'ch13' : forms.NumberInput(attrs={
            'class':'form-control', 'step':'0.1', 'min':'0', 'max':'1'
            }),
            'ch14' : forms.NumberInput(attrs={
            'class':'form-control', 'step':'0.1', 'min':'0', 'max':'1'
            }),
            'keterangan' : forms.Textarea(attrs={
            'class':'form-control','rows':'16'
             }),
            'status_haki' : forms.Select(choices=pil_status_haki,attrs={
            'class':'form-select'
            }),
            'progres': forms.HiddenInput(attrs={
            'class' : 'form-control'
            }),
            }