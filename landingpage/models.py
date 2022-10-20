from django.db import models
import datetime
import os

 
class contact(models.Model):
   no_hp    = models.CharField(max_length=40, null=True)
   email    = models.CharField(max_length=40, null=True)
   ig       = models.CharField(max_length=40, null=True)
   alamat   = models.TextField(blank=True)

def filepath_umkt_press(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/data_umktpress/', filename)

class UmktPress(models.Model):
    umktpress_overview  = models.TextField(blank=True)
    umktpress_flowservice = models.FileField(upload_to = filepath_umkt_press, null=True, blank=True)
