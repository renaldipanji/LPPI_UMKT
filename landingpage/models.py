from django.db import models
import datetime
import os
# Create your models here.
def filepath_workprogramme(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/data_workprogramme/', filename)

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/data_orgstruktur/', filename)

def filepath_visimisi(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/data_orgstruktur/', filename)

class OrgstrukturModel(models.Model):
    orgstruktur_image = models.FileField(upload_to = filepath, null=True, blank=True)

class WorkProgrammeModel(models.Model):
    file_workprogramme = models.FileField(upload_to = filepath_workprogramme, null=True, blank=True)

class VisiMisiModel(models.Model):
    visi = models.TextField(blank =True)
    misi = models.TextField(blank =True)

class JournalsModel(models.Model):
    nidn = models.CharField(max_length=20, null=True)
    nama_dosen = models.CharField(max_length=50, null=True)
    program_studi = models.CharField(max_length=50, null=True)
    fakultas = models.CharField(max_length=50, null=True)
    judul_artikel = models.CharField(max_length=100, null=True)
    tahun = models.CharField(max_length=4, null=True)
    link = models.CharField(max_length=100, null=True)
  
class TextBooksModel(models.Model):
    nidn = models.CharField(max_length=20, null=True)
    nama_dosen = models.CharField(max_length=50, null=True)
    program_studi = models.CharField(max_length=50, null=True)
    fakultas = models.CharField(max_length=50, null=True)
    judul_buku = models.CharField(max_length=100, null=True)
    tahap_luaran_10 = models.BooleanField(default=False)
    tahap_luaran_40 = models.BooleanField(default=False)
    tahap_luaran_80 = models.BooleanField(default=False)
    reviewer = models.CharField(max_length=100, null=True)
    tahun = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=100, null=True)

 
class ContactModel(models.Model):
   no_hp    = models.CharField(max_length=40, null=True)
   email    = models.CharField(max_length=40, null=True)
   ig       = models.CharField(max_length=40, null=True)
   alamat   = models.TextField(blank=True)
   
def filepath_journal_umkt(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/data_journal_umkt/', filename)
 
class JournalUmktModel(models.Model):
    cover_jurnal = models.FileField(upload_to = filepath_journal_umkt, null=True, blank=True)
    judul_jurnal = models.CharField(max_length=50, blank=True)
    issn = models.CharField(max_length=20, blank=True)
    publication = models.CharField(max_length=50, blank=True)
    index = models.TextField(blank=True)
    deskripsi = models.TextField(blank=True)
    link_view_jurnal = models.CharField(max_length=100, blank=True)
    link_current_issue = models.CharField(max_length=100, blank=True)
    link_online_submission = models.CharField(max_length=100, blank=True)
    link_download_template = models.CharField(max_length=100, blank=True)
    jenis_journal = models.CharField(max_length=10, blank=True)
   
def filepath_event(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/data_event/', filename)
 
class EventModel(models.Model):
   event_image = models.FileField(upload_to = filepath_event, null=True, blank=True)

def filepath_divisi(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/data_divisi/', filename)

class DivisiModel(models.Model):
    members_divisi  = models.FileField(upload_to = filepath_divisi, null=True, blank=True)
    overview_divisi = models.TextField(blank=True)

def filepath_service(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/data_service/', filename)

class ServiceModel(models.Model):
    flowservice_service = models.FileField(upload_to = filepath_service, null=True, blank=True)
    overview_service = models.TextField(blank=True)

def filepath_downloads(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/file_download/', filename)

class DownloadContent(models.Model):
    nama_file = models.CharField(max_length = 100, null=True)
    jenis_file = models.CharField(max_length = 100, null=True)
    ukuran_file = models.CharField(max_length = 10, null=True)
    file_download = models.FileField(upload_to = filepath_downloads, null=True, blank=True)