from django.contrib import admin
from django.urls import path,include

from .views import *

urlpatterns = [
    path('visi-misi/', visi_misi, name='visi_misi'),
    path('workprog/', workprog, name='workprog'),
    path('divisi_ppi/', divisi_ppi, name='divisi_ppi'),
    path('divisi_elearning/', divisi_elearning, name='divisi_elearning'),
    path('news/', news, name='news'),
    path('event/', event, name='event'),
]
