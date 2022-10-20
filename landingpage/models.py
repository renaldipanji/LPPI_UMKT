from django.db import models
import datetime
import os

 
class contact(models.Model):
   no_hp    = models.CharField(max_length=40, null=True)
   email    = models.CharField(max_length=40, null=True)
   ig       = models.CharField(max_length=40, null=True)
   alamat   = models.TextField(blank=True)
   
def filepath_journal_serving(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/data_journalserving/', filename)
 
class journal_serving(models.Model):
   member_image = models.FileField(upload_to = filepath_journal_serving, null=True, blank=True)
   overview = models.TextField(blank=True)
   
def filepath_event(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/data_event/', filename)
 
class EventMo(models.Model):
   event_image = models.FileField(upload_to = filepath_event, null=True, blank=True)