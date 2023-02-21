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
    path('elearning/', e_learning, name='e_learning'),

    #>>>>>>>>>>>>>>>>>>>>>>Backend Views <<<<<<<<<<<<<<<<<<<<<<<<<<<

    path('orgstruktur-backend/', orgstruktur_backend, name='orgstruktur_backend'),
    path('workprogramme-backend/', workprogramme_backend, name='workprogramme_backend'),
    path('visimisi-backend/', visimisi_backend, name='visimisi_backend'),
    path('journals-backend/', journals_backend, name='journals_backend'),
    path('textbooks-backend/', textbooks_backend, name='textbooks_backend'),
    path('penelitian-backend/', penelitian_backend, name='penelitian_backend'),
    path('pengabdian-backend/', pengabdian_backend, name='pengabdian_backend'),
    path('master-fakultas-backend/', master_fakultas_backend, name='master_fakultas_backend'),
    path('master-fakultas-backend/delete/<str:id>/', master_fakultas_backend_delete, name='master_fakultas_backend_delete'),
    path('master-fakultas-backend/update/<str:id>/', master_fakultas_backend_update, name='master_fakultas_backend_update'),
    path('master-prodi-backend/', master_prodi_backend, name='master_prodi_backend'),
    path('master-prodi-backend/update/<str:id>/', master_prodi_backend_update, name='master_prodi_backend_update'),
    path('master-prodi-backend/delete/<str:id>/', master_prodi_backend_delete, name='master_prodi_backend_delete'),
    path('master-dosen-backend/', master_dosen_backend, name='master_dosen_backend'),
    path('master-dosen-backend/update/<str:id>', master_dosen_backend_update, name='master_dosen_backend_update'),
    path('master-dosen-backend/delete/<str:id>', master_dosen_backend_delete, name='master_dosen_backend_delete'),
    path('master-mahasiswa-backend/update/<str:id>', master_mahasiswa_backend_update, name='master_mahasiswa_backend_update'),
    path('master-mahasiswa-backend/delete/<str:id>', master_mahasiswa_backend_delete, name='master_mahasiswa_backend_delete'),
    path('master-mahasiswa-backend/', master_mahasiswa_backend, name='master_mahasiswa_backend'),
    path('master-kategori-index-backend/', master_kategori_index_backend, name='master_kategori_index_backend'),
    path('master-kategori-index-backend/delete/<str:id>', master_kategori_index_backend_delete, name='master_kategori_index_backend_delete'),
    path('master-kategori-index-backend/update/<str:id>', master_kategori_index_backend_update, name='master_kategori_index_backend_update'),
    path('contact-backend/', contact_backend, name='contact_backend'),
    path('journal-serving-backend/', journal_serving_backend, name='journal_serving_backend'),
    path('journal-serving-backend/delete/<str:id>/', journal_serving_backend_delete, name='journal_serving_backend_delete'),
    path('journal-serving-backend/update/<str:id>/', journal_serving_backend_update, name='journal_serving_backend_update'),
    path('journal-serving-backend/detail/<str:id>/', journal_serving_backend_detail, name='journal_serving_backend_detail'),
    path('journal-research-backend/', journal_research_backend, name='journal_research_backend'),
    path('journal-research-backend/delete/<str:id>/', journal_research_backend_delete, name='journal_research_backend_delete'),
    path('journal-research-backend/update/<str:id>/', journal_research_backend_update, name='journal_research_backend_update'),
    path('journal-research-backend/detail/<str:id>/', journal_research_backend_detail, name='journal_research_backend_detail'),
    path('event-backend/', event_backend, name='event_backend'),
    path('journals-backend/delete/<str:id>/', journals_backend_delete, name='journals_backend_delete'),
    path('journals-backend/update/<str:id>/', journals_backend_update, name='journals_backend_update'),
    path('textbooks-backend/delete/<str:id>/', textbooks_backend_delete, name='textbooks_backend_delete'),
    path('textbooks-backend/update/<str:id>/', textbooks_backend_update, name='textbooks_backend_update'),
    path('divisippi-backend/', divisippi_backend, name='divisippi_backend'),
    path('divisielearning-backend/', divisielearning_backend, name='divisielearning_backend'),
    path('articletranslation-backend/', articletranslation_backend, name='articletranslation_backend'),
    path('sipena-backend/', sipena_backend, name='sipena_backend'),
    path('umktpress-backend/', umktpress_backend, name='umktpress_backend'),
    path('elearningsupport-backend/', elearningsupport_backend, name='elearningsupport_backend'),
    path('downloads-backend/', downloads_backend, name='downloads_backend'),
    path('downloads-backend-update/<str:id>/', downloads_backend_update, name='downloads_backend_update'),
    path('downloads-backend-delete/<str:id>/', downloads_backend_delete, name='downloads_backend_delete'),

]


if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
