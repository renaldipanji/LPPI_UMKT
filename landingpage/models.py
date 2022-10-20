from django.db import models

# Create your models here.
from django.db import models
import datetime
import os
# Create your models here.
def filepath_orgstruktur(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/data_orgstruktur/', filename)

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/data_orgstruktur/', filename)

class orgstruktur(models.Model):
    file_orgstruktur = models.FileField(upload_to = filepath_orgstruktur, null=True, blank=True)

def filepath_divisi_ppi(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/data_divisippi/', filename)

class divisippi(models.Model):
    member_image = models.FileField(upload_to = filepath_divisi_ppi, null=True, blank=True)
    overview = models.TextField(blank=True)

def filepath_article_translation(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/data_articletranslation/', filename)

class articletranslation(models.Model):
    member_image = models.FileField(upload_to = filepath_article_translation, null=True, blank=True)
    overview = models.TextField(blank=True)

def filepath_sipena(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/data_sipena/', filename)

class sipena(models.Model):
    member_image = models.FileField(upload_to = filepath_sipena, null=True, blank=True)
    overview = models.TextField(blank=True)

def filepath_journal_research(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/data_journalresearch/', filename)

class journalresearch(models.Model):
    cover_jurnal = models.FileField(upload_to = filepath_journal_research, null=True, blank=True)
    judul_jurnal = models.CharField(max_length=50, blank=True)
    issn = models.CharField(max_length=20, blank=True)
    publication = models.CharField(max_length=50, blank=True)
    index = models.TextField(blank=True)
    deskripsi = models.TextField(blank=True)
    link_view_jurnal = models.CharField(max_length=100, blank=True)
    link_current_issue = models.CharField(max_length=100, blank=True)
    link_online_submission = models.CharField(max_length=100, blank=True)
    link_download_template = models.CharField(max_length=100, blank=True)