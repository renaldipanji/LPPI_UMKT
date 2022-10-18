from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name='about'),
    path('visi-misi/', visi_misi, name='visi_misi'),
    path('org_struktur/', org_struktur, name='org_struktur'),
    path('devisi/', devisi, name='devisi'),
    path('contact/', contact, name='contact'),
    path('workprog/', workprog, name='workprog'),
    path('divisi_ppi/', divisi_ppi, name='divisi_ppi'),
    path('divisi_elearning/', divisi_elearning, name='divisi_elearning'),
    path('news/', news, name='news'),
    path('single-news/', news_single, name='news_single'),
    path('event/', event, name='event'),
    path('journal/', journal, name='journal'),
    path('textbook/', textbook, name='textbook'),
    path('newspaper/', newspaper, name='newspaper'),
    path('downloads/', downloads, name='downloads'),
    path('journal-research-umkt/', journal_research_umkt, name='journal_research_umkt'),
    path('journal-social-umkt/', journal_social_umkt, name='journal_social_umkt'),
    path('translate_art/', translate_art, name='translate_art'),
    path('sipena/', sipena, name='sipena'),
    path('umktpress/', umktpress, name='umktpress'),
    path('e_learning/', e_learning, name='e_learning'),

    #>>>>>>>>>>>>BACKEND<<<<<<<<<<<<<
    path('workprogramme-backend/', workprogramme_backend, name='workprogramme_backend'),
    path('visimisi-backend/', visimisi_backend, name='visimisi_backend'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)