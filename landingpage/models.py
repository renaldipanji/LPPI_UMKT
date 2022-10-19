from django.db import models
import datetime
import os

 
class contact(models.Model):
   no_hp    = models.CharField(max_length=40, null=True)
   email    = models.CharField(max_length=40, null=True)
   ig       = models.CharField(max_length=40, null=True)
   alamat   = models.TextField(blank=True)