from django.db import models
import datetime
import os
from django.contrib.auth.models import AbstractUser

def imagepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/profil/', filename)

class User(AbstractUser):
    nama = models.CharField(max_length=150, null=True)
    nidn = models.CharField(max_length=150, null=True, unique=True)
    no_hp = models.CharField(max_length=15, null=True)
    institusi = models.CharField(max_length=2, null=True)
    nama_institusi = models.CharField(max_length=50, blank=True)
    foto_profile = models.ImageField(upload_to = imagepath, null=True, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    forgot_password_token = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True )