from django.contrib import admin
from django.urls import path,include

from .views import *

urlpatterns = [
    path('visi-misi/', visi_misi, name='visi_misi'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
