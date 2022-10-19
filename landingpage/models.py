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
    return os.path.join('uploads/data_workprogramme/', filename)

class Workprogramme(models.Model):
    file_workprogramme = models.FileField(upload_to = filepath_workprogramme, null=True, blank=True)

def filepath_visimisi(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/data_visimisi/', filename)

class Visimisi(models.Model):
    visi = models.TextField(blank =True)
    misi = models.TextField(blank =True)

class Journals(models.Model):
    Nama = models.CharField(max_length=50, null=True)
    Judul_Artikel = models.CharField(max_length=100, null=True)
    Tahun    = models.CharField(max_length=4, null=True)
    Link    = models.CharField(max_length=100, null=True)
  
