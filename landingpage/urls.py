from django.contrib import admin
from django.urls import path,include

from .views import *

urlpatterns = [
    path('visi-misi/', visi_misi, name='visi_misi'),
    path('workprog/', workprog, name='workprog'),
    path('divisi_ppi/', divisi_ppi, name='divisi_ppi'),
    path('divisi_elearning/', divisi_elearning, name='divisi_elearning'),
    path('event/', event, name='event'),
    path('translate_art/', translate_art, name='translate_art'),
    path('sipena/', sipena, name='sipena'),
    path('isbn/', isbn, name='isbn'),
    path('umktpress/', umktpress, name='umktpress'),
    path('e_learning/', e_learning, name='e_learning'),
]

