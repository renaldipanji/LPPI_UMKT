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
    nama = models.CharField(max_length=50, null=True)
    judul_artikel = models.CharField(max_length=100, null=True)
    tahun = models.CharField(max_length=4, null=True)
    link = models.CharField(max_length=100, null=True)
  
class TextBooksModel(models.Model):
    program_studi = models.CharField(max_length=50, null=True)
    nama = models.CharField(max_length=50, null=True)
    judul_buku = models.CharField(max_length=100, null=True)
    tahap_luaran_10 = models.BooleanField(default=False)
    tahap_luaran_40 = models.BooleanField(default=False)
    tahap_luaran_80 = models.BooleanField(default=False)
    reviewer = models.CharField(max_length=100, null=True)
    tahun = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=100, null=True)
