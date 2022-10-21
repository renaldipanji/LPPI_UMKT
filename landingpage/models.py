from django.db import models
import datetime
import os
# Create your models here.
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/file_download/', filename)

class DownloadContent(models.Model):
    nama_file = models.CharField(max_length = 100, null=True)
    jenis_file = models.CharField(max_length = 10, null=True)
    ukuran_file = models.CharField(max_length = 10, null=True)
    file_download = models.FileField(upload_to = filepath, null=True, blank=True)
    