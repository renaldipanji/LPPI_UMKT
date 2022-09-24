from django.contrib import admin
from django.urls import path,include

from .views import *

urlpatterns = [
    path('', index),
    path('about/', about, name='about'),
    path('visi-misi/', visi_misi, name='visi_misi'),
    path('org_struktur/', org_struktur, name='org_struktur'),
    path('devisi/', devisi, name='devisi'),
    path('contact/', contact, name='contact'),
]
