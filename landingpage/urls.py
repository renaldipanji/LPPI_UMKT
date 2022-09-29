from django.contrib import admin
from django.urls import path,include

from .views import *

urlpatterns = [
    path('visi-misi/', visi_misi, name='visi_misi'),
    path('about/', about, name='about'),
    path('journal/', journal, name='journal'),
    path('textbook/', textbook, name='textbook'),
    path('newspaper/', newspaper, name='newspaper'),
    path('downloads/', downloads, name='downloads'),
]
