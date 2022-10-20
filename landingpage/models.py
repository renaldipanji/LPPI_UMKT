from django.db import models

# Create your models here.
from django.db import models
import datetime
import os
# Create your models here.
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/data_orgstruktur/', filename)

class OrgstrukturModel(models.Model):
    orgstruktur_image = models.FileField(upload_to = filepath, null=True, blank=True)

