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
 
class JournalServingModel(models.Model):
      cover_jurnal = models.FileField(upload_to = filepath_journal_serving, null=True, blank=True)
      judul_jurnal = models.CharField(max_length=50, blank=True)
      issn = models.CharField(max_length=20, blank=True)
      publication = models.CharField(max_length=50, blank=True)
      index = models.TextField(blank=True)
      deskripsi = models.TextField(blank=True)
      link_view_jurnal = models.CharField(max_length=100, blank=True)
      link_current_issue = models.CharField(max_length=100, blank=True)
      link_online_submission = models.CharField(max_length=100, blank=True)
      link_download_template = models.CharField(max_length=100, blank=True)
   # member_image = models.FileField(upload_to = filepath_journal_serving, null=True, blank=True)
   # overview = models.TextField(blank=True)