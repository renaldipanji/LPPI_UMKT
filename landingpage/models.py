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
   
def filepath_journal_serving(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/data_journalserving/', filename)
 
class Journal_ServingModel(models.Model):
   member_image = models.FileField(upload_to = filepath_journal_serving, null=True, blank=True)
   overview = models.TextField(blank=True)
   
def filepath_event(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/data_event/', filename)
 
class EventModel(models.Model):
   event_image = models.FileField(upload_to = filepath_event, null=True, blank=True)
