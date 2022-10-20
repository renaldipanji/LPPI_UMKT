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

def filepath_divisi_elearning(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/data_divisielearning/', filename)

class divisielearning(models.Model):
    flowservice_divisielearning = models.FileField(upload_to = filepath_divisi_elearning, null=True, blank=True)
    overview_divisielearning = models.TextField(blank=True)