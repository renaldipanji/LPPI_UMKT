from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('login/', views.login, name= 'login'),
    path('logout/', views.logout_view, name= 'logout'),
    path('profil/', views.profil, name='profil'),
    path('daftar/', views.daftar, name='daftar'),
    path('lupa-password/', views.lupaPassword, name='lupaPassword'),
    path('change-password/<token>/', views.changePassword, name='change_password'),
    path('konfirmasi-reset-password/', TemplateView.as_view(template_name='akun/konf_email_reset_password.html'), name='konfirmasi_reset_pass'),
    path('daftar-berhasil/', TemplateView.as_view(template_name='akun/daftar_berhasil.html'), name='daftar_berhasil'),
    path('dashboard/', TemplateView.as_view(template_name='akun/dashboard.html'), name='dashboard'),
    path('verifikasi-berhasil/<token>/', views.verifBerhasil, name='verif_berhasil'),
    path('reset-password-berhasil/', TemplateView.as_view(template_name='akun/reset_password_berhasil.html')),
    path('konfirmasi-verifikasi-akun/', views.konfVerifAkun, name='konfirm_verif_akun'),
    path('verifikasi-akun/', views.verifAkun, name='verifikasi_akun'),
]
