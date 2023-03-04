from .forms import *
from .models import *
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import time
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q

def about(request):
    return render(request,'landingpage/frontend/about.html')

def visi_misi(request):
    data = VisiMisiModel.objects.get(id='1')
    context ={
        'data':data,
    }
    return render(request,'landingpage/frontend/visi_misi.html', context)
    
def index(request):
    return render(request,'landingpage/frontend/index.html')

def org_struktur(request):
    data = OrgstrukturModel.objects.get(id='2')
    context ={
        'data': data,
    }
    return render(request,'landingpage/frontend/org_struktur.html', context)

def devisi(request):
    return render(request,'landingpage/frontend/devisi.html')

def contact(request):
    data = ContactModel.objects.get(id='1')
    context ={
        'data': data,
    }
    return render(request, 'landingpage/frontend/contact.html',context)

def workprog(request):
    data = WorkProgrammeModel.objects.get(id='1')
    context ={
        'data': data,
    }
    return render(request,'landingpage/frontend/workprog.html', context)

def divisi_ppi(request):
    data = DivisiModel.objects.get(id='1')
    context ={
        'data': data,
    }
    return render(request,'landingpage/frontend/divisi_ppi.html',context)

def divisi_elearning(request):
    data = DivisiModel.objects.get(id='2')
    context ={
        'data': data,
    }
    return render(request, 'landingpage/frontend/divisi_elearning.html',context)

def news(request):
    return render(request, 'landingpage/frontend/news.html')

def news_single(request):
    return render(request, 'landingpage/frontend/news_single.html')

def event(request):
    data = EventModel.objects.get(id='1')
    context ={
        'data': data,
    }
    return render(request, 'landingpage/frontend/event.html',context)
    
def penelitian(request):
    if request.method == "GET":
        if request.GET.get('dosen'):
            dosen = request.GET.get('dosen')
            data_research = PenelitianDosenModel.objects.filter(Q(ketua_peneliti=dosen) | Q(anggotapenelitidosenmodel__anggota_dosen=dosen))
        elif request.GET.get('prodi'):
            prodi = request.GET.get('prodi')
            data_research = PenelitianDosenModel.objects.select_related('prodi').filter(prodi=prodi)
        elif request.GET.get('akreditasi'):
            akreditasi = request.GET.get('akreditasi')
            data_research = PenelitianDosenModel.objects.select_related('kategori_index').filter(kategori_index=akreditasi)
        elif request.GET.get('tahun'):
            tahun = request.GET.get('tahun')
            data_research = PenelitianDosenModel.objects.filter(tahun=tahun)
        else:
            data_research = PenelitianDosenModel.objects.all()
        for research in data_research:
            research.anggota_peneliti = AnggotaPenelitiDosenModel.objects.filter(penelitian=research)

    data_prodi = ProdiModel.objects.all()
    context ={
        'data_research': data_research,
        'data_prodi': data_prodi,
    }   
    return render(request, 'landingpage/frontend/penelitian.html',context)

def pengabdian(request):
    if request.method == "GET":
        if request.GET.get('dosen'):
            dosen = request.GET.get('dosen')
            data_research = PengabdianDosenModel.objects.filter(Q(ketua_peneliti=dosen) | Q(anggotapengabdiandosenmodel__anggota_dosen=dosen)) 
        elif request.GET.get('prodi'):
            prodi = request.GET.get('prodi')
            data_research = PengabdianDosenModel.objects.select_related('prodi').filter(prodi=prodi)
        elif request.GET.get('tahun'):
            tahun = request.GET.get('tahun')
            data_research = PengabdianDosenModel.objects.filter(tahun=tahun)
        else:
            data_research = PengabdianDosenModel.objects.select_related('ketua_peneliti').all()
        for research in data_research:
            research.anggota_peneliti = AnggotaPengabdianDosenModel.objects.filter(pengabdian=research)
    data_prodi = ProdiModel.objects.all()
    context ={
        'data_research': data_research,
        'data_prodi': data_prodi,
    }   
    return render(request, 'landingpage/frontend/pengabdian.html',context)

def newspaper(request):
    return render(request, 'landingpage/frontend/newspaper.html')

def textbook(request):
    data = TextBooksModel.objects.all()
    context ={
        'data_textbook': data,
    }    
    return render(request, 'landingpage/frontend/textbook.html',context)

def downloads(request):
    data = DownloadContent.objects.all()
    context={
        'data_downloads':data,
    }
    return render(request, 'landingpage/frontend/downloads.html',context)

def journal_research_umkt(request):
    data = JournalUmktModel.objects.all().filter(jenis_journal='research')
    context ={
        'data_journal' : data,
    }
    return render(request, 'landingpage/frontend/jurnal_penelitian_umkt.html', context)

def journal_social_umkt(request):
    data = JournalUmktModel.objects.all().filter(jenis_journal='serving')
    context ={
        'data_journal' : data,
    }
    return render(request, 'landingpage/frontend/jurnal_pengabdian_umkt.html',context)

def translate_art(request):
    return render(request, 'landingpage/frontend/translate_art.html')

def sipena(request):
    return render(request, 'landingpage/frontend/sipena.html')

def umktpress(request):
    return render(request, 'landingpage/frontend/umktpress.html')

def e_learning(request):
    return render(request, 'landingpage/frontend/e_learning.html')

    #>>>>>>>>>>>>>>>> Backend Views <<<<<<<<<<<<<<<<<<<<<

def orgstruktur_backend (request):
    orgstruktur_update = OrgstrukturModel.objects.get(id='2')
    data = {
        'orgstruktur_image' : orgstruktur_update.orgstruktur_image,
    }
    orgstruktur_form = OrgstrukturForm(request.POST or None, request.FILES  or None, initial=data, instance=orgstruktur_update)

    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'orgstruktur_image' in result_request
        if cek_image == False:
            if orgstruktur_update.orgstruktur_image:
                if os.path.isfile(orgstruktur_update.orgstruktur_image.path) == True:
                    os.remove(orgstruktur_update.orgstruktur_image.path)
        if orgstruktur_form.is_valid():
            orgstruktur_form.save()
            messages.info(request, 'Data Struktur Organisasi Berhasil di Edit')
            return redirect('orgstruktur_backend')
    context = {
        'form': orgstruktur_form,
        'data': orgstruktur_update,
    }
    return render(request, 'landingpage/backend/orgstruktur_backend.html', context)

def workprogramme_backend (request):
    workprogramme_update = WorkProgrammeModel.objects.get(id='1')
    data = {
        'file_workprogramme' : workprogramme_update.file_workprogramme,
    }
    workprogramme_form = WorkProgrammeForm(request.POST or None, request.FILES  or None, initial=data, instance=workprogramme_update)

    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'file_workprogramme' in result_request
        if cek_image == False:
            if workprogramme_update.file_workprogramme:
                if os.path.isfile(workprogramme_update.file_workprogramme.path) == True:
                    os.remove(workprogramme_update.file_workprogramme.path)
        if workprogramme_form.is_valid():
            workprogramme_form.save()
            messages.success(request, 'Data Program Kerja Berhasil di Update')
            return redirect('workprogramme_backend')
    context = {
        'form' : workprogramme_form,
        'data' : data,
    }
    return render(request, 'landingpage/backend/workprogramme_backend.html', context)

def visimisi_backend (request):
    visimisi_update = VisiMisiModel.objects.get(id='1')
    data = {
        'visi' : visimisi_update.visi,
        'misi' : visimisi_update.misi,
    }
    visimisi_form = VisiMisiForm(request.POST or None, initial=data, instance=visimisi_update)
    if request.method == "POST":
            visimisi_form.save()
            messages.info(request, 'Data Visi Misi Berhasil di Edit')
    context = {
        'form' : visimisi_form,
        'data' : visimisi_update,
    }
    return render(request, 'landingpage/backend/visimisi_backend.html', context)

def journals_backend (request):
    data = JournalsModel.objects.all()
    journals_form = JournalsForm(request.POST or None)
    if request.method == "POST" and journals_form.is_valid():
        journals_form.save()
        messages.info(request, 'Data Journals Berhasil di Edit')
        redirect('journals_backend')
    else :
        print(journals_form.errors)

    context = {
        'form' : journals_form,
        'Data' : data,
    }
    return render(request, 'landingpage/backend/journals_backend.html', context)

def journals_backend_delete(request, id):
    JournalsModel.objects.filter(id=id).delete()
    messages.error(request, 'Data Journals Berhasil di Hapus')
    return redirect('journals_backend')

def journals_backend_update (request, id):
    journals_edit = JournalsModel.objects.get(id=id)

    data_edit = {
        'nidn' : journals_edit.nidn,
        'nama_dosen' : journals_edit.nama_dosen,
        'program_studi' : journals_edit.program_studi,
        'fakultas' : journals_edit.fakultas,
        'judul_artikel' : journals_edit.judul_artikel,
        'tahun' : journals_edit.tahun,
        'link' : journals_edit.link,
    }
    journals_form_edit = JournalsForm(request.POST or None, initial=data_edit, instance=journals_edit) 

    if request.method == "POST" and journals_form_edit.is_valid():
        journals_form_edit.save()
        messages.info(request, 'Data Text Books Berhasil di Edit')
        return redirect('journals_backend')
    else :
        print(journals_form_edit.errors)

    context = {
        'form' : journals_form_edit,
    }

    return render(request, 'landingpage/backend/journals_backend_update.html', context)

def textbooks_backend (request):
    data = TextBooksModel.objects.all()
    textbooks_form = TextBookForm(request.POST or None)
    if request.method == "POST" and textbooks_form.is_valid():
        textbooks_form.save()
        messages.success(request, 'Data Text Books Berhasil di Tambahkan')
        redirect('textbooks_backend')
    else :
        print(textbooks_form.errors)

    context = {
        'form' : textbooks_form,
        'Data' : data,
    }
    return render(request, 'landingpage/backend/textbooks_backend.html', context)
    return render(request, 'landingpage/e_learning.html')

def penelitian_backend(request):
    form = PenelitianDosenForm(request.POST or None)
    data = PenelitianDosenModel.objects.all()
    dosen = DosenModel.objects.all()
    mahasiswa = MahasiswaModel.objects.all()
    if request.method == 'POST' and form.is_valid():
        # Logic Simpan Penelitian
        id_dosen = request.POST['ketua_peneliti']
        data_dosen = DosenModel.objects.get(id=id_dosen)
        penelitian_form = form.save(commit=False)
        penelitian_form.fakultas = data_dosen.fakultas
        penelitian_form.prodi = data_dosen.prodi
        penelitian_form.save()
        messages.success(request, 'Data Penelitian Berhasil di Tambahkan')
        return redirect('penelitian_backend_detail', penelitian_form.id)
    else:
        print(form.errors)
        
    context = {
        'form': form,
        'Data':data,
    }
    return render(request, 'landingpage/backend/penelitian_backend.html', context)

@require_POST
@csrf_protect
def penelitian_backend_delete(request, id):
    data = get_object_or_404(PenelitianDosenModel,id=id)
    data.delete()  
    messages.error(request, 'Data Penelitian Berhasil di Hapus')
    return redirect('penelitian_backend')

def anggota_penelitian_mahasiswa_delete(request, id):
    data = get_object_or_404(AnggotaPenelitiMahasiswaModel,id=id)
    data.delete()  
    messages.error(request, 'Anggota Peneliti (Mahasiswa) Berhasil di Hapus')
    return redirect('penelitian_backend_detail', data.penelitian.id) 

def anggota_penelitian_dosen_delete(request, id):
    data = get_object_or_404(AnggotaPenelitiDosenModel,id=id)
    data.delete()  
    messages.error(request, 'Anggota Peneliti (Dosen) Berhasil di Hapus')
    return redirect('penelitian_backend_detail', data.penelitian.id) 

def tambah_anggota_penelitian_mhs(request, id):
    form_mahasiswa = AnggotaPenelitiMahasiswaForm(request.POST or None)
    if request.method == 'POST' and form_mahasiswa.is_valid():
        # Logic Simpan Penelitian
        id_mahasiswa = request.POST['anggota_mahasiswa']
        if AnggotaPenelitiMahasiswaModel.objects.filter(anggota_mahasiswa=id_mahasiswa,penelitian=id).exists():
            messages.error(request, 'Anggota Penelitian (Mahasiswa) Sudah ada')
            return redirect('penelitian_backend_detail', id)
        if PenelitianDosenModel.objects.filter(anggota_mahasiswa=id_mahasiswa,id=id).exists():
            messages.error(request, 'Anggota Penelitian (Mahasiswa) Sudah ada')
            return redirect('penelitian_backend_detail', id)
        else:
            penelitian = PenelitianDosenModel.objects.get(id=id)
            data_mahasiswa = MahasiswaModel.objects.get(id=id_mahasiswa)
            penelitian_form = form_mahasiswa.save(commit=False)
            penelitian_form.penelitian = penelitian
            penelitian_form.fakultas = data_mahasiswa.fakultas
            penelitian_form.prodi = data_mahasiswa.prodi
            penelitian_form.save()
            messages.success(request, 'Anggota Penelitian (Mahasiswa) Berhasil di Tambahkan')
            return redirect('penelitian_backend_detail', id)    
        
def penelitian_backend_detail(request, id):
    data = get_object_or_404(PenelitianDosenModel,id=id)
    data_anggota_dosen = AnggotaPenelitiDosenModel.objects.select_related('anggota_dosen').filter(penelitian=id)
    data_anggota_mahasiswa = AnggotaPenelitiMahasiswaModel.objects.select_related('anggota_mahasiswa').filter(penelitian=id)
    form_dosen = AnggotaPenelitiDosenForm(request.POST or None)
    form_mahasiswa = AnggotaPenelitiMahasiswaForm(request.POST or None)
    if request.method == 'POST' and form_dosen.is_valid():
        # Logic Simpan Penelitian
        id_dosen = request.POST['anggota_dosen']
        if AnggotaPenelitiDosenModel.objects.filter(anggota_dosen=id_dosen,penelitian=id).exists():
            messages.error(request, 'Anggota Penelitian (Dosen) Sudah ada')
            redirect('penelitian_backend_detail', id)
        else:
            penelitian = PenelitianDosenModel.objects.get(id=id)
            data_dosen = DosenModel.objects.get(id=id_dosen)
            penelitian_form = form_dosen.save(commit=False)
            penelitian_form.penelitian = penelitian
            penelitian_form.fakultas = data_dosen.fakultas
            penelitian_form.prodi = data_dosen.prodi
            penelitian_form.save()
            messages.success(request, 'Anggota Penelitian (Dosen) Berhasil di Tambahkan')
            redirect('penelitian_backend_detail', id)
    else:
        print(form_dosen.errors)
        
    context = {
        'Data':data,
        'aksi':'detail',
        'form_dosen': form_dosen,
        'form_mahasiswa': form_mahasiswa,
        'data_anggota_dosen':data_anggota_dosen,
        'data_anggota_mahasiswa':data_anggota_mahasiswa,
    }
    return render(request, 'landingpage/backend/penelitian_backend_detail.html', context)

def penelitian_backend_update(request, id):
    object_data = get_object_or_404(PenelitianDosenModel,id=id)
    data_anggota_dosen = AnggotaPenelitiDosenModel.objects.select_related('anggota_dosen').filter(penelitian=id)
    data_anggota_mahasiswa = AnggotaPenelitiMahasiswaModel.objects.select_related('anggota_mahasiswa').filter(penelitian=id)
    form_dosen = AnggotaPenelitiDosenForm(request.POST or None)
    form_mahasiswa = AnggotaPenelitiMahasiswaForm(request.POST or None)
    data_edit = {
        'judul' : object_data.judul,
        'tahun' : object_data.tahun,
        'penyedia_jurnal' : object_data.penyedia_jurnal,
        'kategori_index' : object_data.kategori_index,
        'asal_pendanaan' : object_data.asal_pendanaan,
        'total_pendanaan' : object_data.total_pendanaan,
        'link_publikasi' : object_data.link_publikasi,
        'ketua_peneliti' : object_data.ketua_peneliti,
    }
    form_edit = PenelitianDosenForm(request.POST or None, initial=data_edit, instance=object_data) 

    if request.method == "POST" and form_edit.is_valid():
        form_edit.save()
        messages.info(request, 'Data Penelitian Berhasil di Edit')
        return redirect('penelitian_backend')
    else :
        print(form_edit.errors)

    context = {
        'form_edit' : form_edit,
        'aksi' : 'update',
        'form_dosen': form_dosen,
        'Data': object_data,
        'form_mahasiswa': form_mahasiswa,
        'data_anggota_dosen':data_anggota_dosen,
        'data_anggota_mahasiswa':data_anggota_mahasiswa,
    }

    return render(request, 'landingpage/backend/penelitian_backend_detail.html', context)

def pengabdian_backend_detail(request, id):
    data = get_object_or_404(PengabdianDosenModel,id=id)
    data_anggota_dosen = AnggotaPengabdianDosenModel.objects.select_related('anggota_dosen').filter(pengabdian=id)
    data_anggota_mahasiswa = AnggotaPengabdianMahasiswaModel.objects.select_related('anggota_mahasiswa').filter(pengabdian=id)
    form_dosen = AnggotaPengabdianDosenForm(request.POST or None)
    form_mahasiswa = AnggotaPengabdianMahasiswaForm(request.POST or None)
    if request.method == 'POST' and form_dosen.is_valid():
        # Logic Simpan Penelitian
        id_dosen = request.POST['anggota_dosen']
        if AnggotaPengabdianDosenModel.objects.filter(anggota_dosen=id_dosen,pengabdian=id).exists():
            messages.error(request, 'Anggota Penelitian (Dosen) Sudah ada')
            redirect('pengabdian_backend_detail', id)
        else:
            pengabdian = PengabdianDosenModel.objects.get(id=id)
            data_dosen = DosenModel.objects.get(id=id_dosen)
            pengabdian_form = form_dosen.save(commit=False)
            pengabdian_form.pengabdian = pengabdian
            pengabdian_form.fakultas = data_dosen.fakultas
            pengabdian_form.prodi = data_dosen.prodi
            pengabdian_form.save()
            messages.success(request, 'Anggota Pengabdian (Dosen) Berhasil di Tambahkan')
            redirect('pengabdian_backend_detail', id)
    else:
        print(form_dosen.errors)
        
    context = {
        'Data':data,
        'aksi':'detail',
        'form_dosen': form_dosen,
        'form_mahasiswa': form_mahasiswa,
        'data_anggota_dosen':data_anggota_dosen,
        'data_anggota_mahasiswa':data_anggota_mahasiswa,
    }
    return render(request, 'landingpage/backend/pengabdian_backend_detail.html', context)

def anggota_pengabdian_mahasiswa_delete(request, id):
    data = get_object_or_404(AnggotaPengabdianMahasiswaModel,id=id)
    data.delete()  
    messages.error(request, 'Anggota Pengabdian (Mahasiswa) Berhasil di Hapus')
    return redirect('pengabdian_backend_detail', data.pengabdian.id) 

def anggota_pengabdian_dosen_delete(request, id):
    data = get_object_or_404(AnggotaPengabdianDosenModel,id=id)
    data.delete()  
    messages.error(request, 'Anggota Pengabdian (Dosen) Berhasil di Hapus')
    return redirect('pengabdian_backend_detail', data.pengabdian.id) 

def tambah_anggota_pengabdian_mhs(request, id):
    form_mahasiswa = AnggotaPengabdianMahasiswaForm(request.POST or None)
    if request.method == 'POST' and form_mahasiswa.is_valid():
        # Logic Simpan Penelitian
        id_mahasiswa = request.POST['anggota_mahasiswa']
        if AnggotaPengabdianMahasiswaModel.objects.filter(anggota_mahasiswa=id_mahasiswa,pengabdian=id).exists():
            messages.error(request, 'Anggota Pengabdian (Mahasiswa) Sudah ada')
            return redirect('pengabdian_backend_detail', id)
        else:
            pengabdian = PengabdianDosenModel.objects.get(id=id)
            data_mahasiswa = MahasiswaModel.objects.get(id=id_mahasiswa)
            pengabdian_form = form_mahasiswa.save(commit=False)
            pengabdian_form.pengabdian = pengabdian
            pengabdian_form.fakultas = data_mahasiswa.fakultas
            pengabdian_form.prodi = data_mahasiswa.prodi
            pengabdian_form.save()
            messages.success(request, 'Anggota Pengabdian (Mahasiswa) Berhasil di Tambahkan')
            return redirect('pengabdian_backend_detail', id)   

def pengabdian_backend_update(request, id):
    object_data = get_object_or_404(PengabdianDosenModel,id=id)
    data_anggota_dosen = AnggotaPengabdianDosenModel.objects.select_related('anggota_dosen').filter(pengabdian=id)
    data_anggota_mahasiswa = AnggotaPengabdianMahasiswaModel.objects.select_related('anggota_mahasiswa').filter(pengabdian=id)
    form_dosen = AnggotaPengabdianDosenForm(request.POST or None)
    form_mahasiswa = AnggotaPengabdianMahasiswaForm(request.POST or None)
    data_edit = {
        'judul' : object_data.judul,
        'tahun' : object_data.tahun,
        'asal_pendanaan' : object_data.asal_pendanaan,
        'total_pendanaan' : object_data.total_pendanaan,
        'link_laporan' : object_data.link_laporan,
        'ketua_peneliti' : object_data.ketua_peneliti,
    }
    form_edit = PengabdianDosenForm(request.POST or None, initial=data_edit, instance=object_data) 

    if request.method == "POST" and form_edit.is_valid():
        form_edit.save()
        messages.info(request, 'Data Pengabdian Berhasil di Edit')
        return redirect('pengabdian_backend')
    else :
        print(form_edit.errors)

    context = {
        'form_edit' : form_edit,
        'aksi' : 'update',
        'form_dosen': form_dosen,
        'Data': object_data,
        'form_mahasiswa': form_mahasiswa,
        'data_anggota_dosen':data_anggota_dosen,
        'data_anggota_mahasiswa':data_anggota_mahasiswa,
    }

    return render(request, 'landingpage/backend/pengabdian_backend_detail.html', context)

@require_POST
@csrf_protect
def pengabdian_backend_delete(request, id):
    data = get_object_or_404(PengabdianDosenModel,id=id)
    data.delete()  
    messages.error(request, 'Data Pengabdian Berhasil di Hapus')
    return redirect('pengabdian_backend')

def pengabdian_backend(request):
    form = PengabdianDosenForm(request.POST or None)
    data = PengabdianDosenModel.objects.all()
    dosen = DosenModel.objects.all()
    mahasiswa = MahasiswaModel.objects.all()
    if request.method == 'POST' and form.is_valid():
        # Logic Simpan Penelitian
        id_dosen = request.POST['ketua_peneliti']
        data_dosen = DosenModel.objects.get(id=id_dosen)
        pengabdian_form = form.save(commit=False)
        pengabdian_form.fakultas = data_dosen.fakultas
        pengabdian_form.prodi = data_dosen.prodi
        pengabdian_form.save()
        messages.success(request, 'Data Penelitian Berhasil di Tambahkan')
        return redirect('pengabdian_backend_detail',pengabdian_form.id)
    else:
        print(form.errors)
        
    context = {
        'form': form,
        'Data':data,
    }
    return render(request, 'landingpage/backend/pengabdian_backend.html', context)

def master_fakultas_backend(request):
    data = FakultasModel.objects.all()
    fakultas_form = FakultasForm(request.POST or None)
    if request.method == "POST" and fakultas_form.is_valid():
        fakultas_form.save()
        messages.success(request, 'Data Fakultas Berhasil di Tambahkan')
        redirect('master_fakultas_backend')
    else :
        print(fakultas_form.errors)
    
    context = {
        'Data' : data,
        'form' : fakultas_form,
        'action' : 'create',
    }

    return render(request, "landingpage/backend/master_fakultas_backend.html", context)

def master_fakultas_backend_update(request,id):
    fakultas_edit = FakultasModel.objects.get(id=id)

    data_edit = {
        'nama_fakultas' : fakultas_edit.nama_fakultas,
    }
    fakultas_form_edit = FakultasForm(request.POST or None, initial=data_edit, instance=fakultas_edit) 

    if request.method == "POST" and fakultas_form_edit.is_valid():
        fakultas_form_edit.save()
        messages.info(request, 'Data Fakultas Berhasil di Edit')
        return redirect('master_fakultas_backend')
    else :
        print(fakultas_form_edit.errors)

    context = {
        'form_edit' : fakultas_form_edit,
        'action' : 'update',
    }

    return render(request, "landingpage/backend/master_fakultas_backend.html", context)

def master_fakultas_backend_delete(request, id):
    FakultasModel.objects.filter(id=id).delete()
    messages.error(request, 'Data Fakultas Berhasil di Hapus')
    return redirect('master_fakultas_backend')

def master_prodi_backend(request):
    data = ProdiModel.objects.select_related('fakultas')
    prodi_form = ProdiForm(request.POST or None)

    if request.method == "POST" and prodi_form.is_valid():
        prodi_form.save()
        messages.info(request, 'Data Prodi Berhasil ditambahkan')
        return redirect('master_prodi_backend')
    else :
        print(prodi_form.errors)

    context={
        'Data': data,
        'form': prodi_form,
        'action': 'create',
    }
    return render(request, "landingpage/backend/master_prodi_backend.html", context)

def master_prodi_backend_update(request,id):
    prodi_edit = ProdiModel.objects.get(id=id)

    data_edit = {
        'fakultas' : prodi_edit.fakultas,
        'nama_prodi' : prodi_edit.nama_prodi,
    }
    prodi_form_edit = ProdiForm(request.POST or None, initial=data_edit, instance=prodi_edit) 

    if request.method == "POST" and prodi_form_edit.is_valid():
        prodi_form_edit.save()
        messages.info(request, 'Data Fakultas Berhasil di Edit')
        return redirect('master_prodi_backend')
    else :
        print(prodi_form_edit.errors)

    context = {
        'form_edit' : prodi_form_edit,
        'action' : 'update',
    }

    return render(request, "landingpage/backend/master_prodi_backend.html", context)

def master_prodi_backend_delete(request, id):
    ProdiModel.objects.filter(id=id).delete()
    messages.error(request, 'Data Prodi Berhasil di Hapus')
    return redirect('master_prodi_backend')

def master_dosen_backend(request):
    data = DosenModel.objects.all()
    dosen_form = DosenForm(request.POST or None)

    if request.method == "POST" and dosen_form.is_valid():
        id_prodi = request.POST['prodi']
        id_fakultas = ProdiModel.objects.get(id=id_prodi)
        dosen =  dosen_form.save(commit=False)
        dosen.fakultas = id_fakultas.fakultas
        dosen.save()
        messages.info(request, 'Data Dosen Berhasil ditambahkan')
        return redirect('master_dosen_backend')
    else :
        print(dosen_form.errors)

    context = {
        'Data':data,
        'form': dosen_form,
        'action': 'create',
    }
    return render(request, "landingpage/backend/master_dosen_backend.html", context)

def master_kategori_index_backend(request):
    data = KategoriIndexModel.objects.all()
    kategori_index_form = KategoriIndexForm(request.POST or None)

    if request.method == "POST" and kategori_index_form.is_valid():
        kategori_index_form.save()
        messages.info(request, 'Data Kategori Index Berhasil ditambahkan')
        return redirect('master_kategori_index_backend')
    else :
        print(kategori_index_form.errors)

    context = {
        'Data':data,
        'form': kategori_index_form,
        'action': 'create',
    }
    return render(request, "landingpage/backend/master_kategori_index_backend.html", context)

def master_kategori_index_backend_delete(request, id):
    KategoriIndexModel.objects.filter(id=id).delete()
    messages.error(request, 'Data Kategori Index Berhasil di Hapus')
    return redirect('master_kategori_index_backend')

def master_kategori_index_backend_update(request,id):
    kategori_index_edit = KategoriIndexModel.objects.get(id=id)

    data_edit = {
        'nama' : kategori_index_edit.nama,
    }
    kategori_index_form_edit = KategoriIndexForm(request.POST or None, initial=data_edit, instance=kategori_index_edit) 

    if request.method == "POST" and kategori_index_form_edit.is_valid():
        kategori_index_form_edit.save()
        messages.info(request, 'Data Kategori Index Berhasil di Edit')
        return redirect('master_kategori_index_backend')
    else :
        print(kategori_index_form_edit.errors)

    context = {
        'form_edit' : kategori_index_form_edit,
        'action' : 'update',
    }
    return render(request, "landingpage/backend/master_kategori_index_backend.html", context)

def master_dosen_backend_update(request,id):
    dosen_edit = DosenModel.objects.get(id=id)

    data_edit = {
        'nidn' : dosen_edit.nidn,
        'nama' : dosen_edit.nama,
        'prodi' : dosen_edit.prodi,
    }
    dosen_form_edit = DosenForm(request.POST or None, initial=data_edit, instance=dosen_edit) 

    if request.method == "POST" and dosen_form_edit.is_valid():
        id_prodi = request.POST['prodi']
        id_fakultas = ProdiModel.objects.get(id=id_prodi)
        dosen = dosen_form_edit.save(commit=False)
        dosen.fakultas  = id_fakultas.fakultas
        dosen.save()
        messages.info(request, 'Data dosen Berhasil di Edit')
        return redirect('master_dosen_backend')
    else :
        print(dosen_form_edit.errors)

    context = {
        'form_edit' : dosen_form_edit,
        'action' : 'update',
    }
    return render(request, "landingpage/backend/master_dosen_backend.html", context)

def master_dosen_backend_delete(request, id):
    DosenModel.objects.filter(id=id).delete()
    messages.error(request, 'Data Dosen Berhasil di Hapus')
    return redirect('master_dosen_backend')

def master_mahasiswa_backend(request):
    data = MahasiswaModel.objects.all()
    mahasiswa_form = MahasiswaForm(request.POST or None)

    if request.method == "POST" and mahasiswa_form.is_valid():
        id_prodi = request.POST['prodi']
        id_fakultas = ProdiModel.objects.get(id=id_prodi)
        mahasiswa =  mahasiswa_form.save(commit=False)
        mahasiswa.fakultas = id_fakultas.fakultas
        mahasiswa.save()
        messages.info(request, 'Data Mahasiswa Berhasil ditambahkan')
        return redirect('master_mahasiswa_backend')
    else :
        print(mahasiswa_form.errors)

    context = {
        'Data':data,
        'form': mahasiswa_form,
        'action' : 'create',
    }    
    return render(request, "landingpage/backend/master_mahasiswa_backend.html", context)

def master_mahasiswa_backend_update(request,id):
    mahasiswa_edit = MahasiswaModel.objects.get(id=id)

    data_edit = {
        'nim' : mahasiswa_edit.nim,
        'nama' : mahasiswa_edit.nama,
        'angkatan' : mahasiswa_edit.angkatan,
        'prodi' : mahasiswa_edit.prodi,
    }
    mahasiswa_form_edit = MahasiswaForm(request.POST or None, initial=data_edit, instance=mahasiswa_edit) 

    if request.method == "POST" and mahasiswa_form_edit.is_valid():
        id_prodi = request.POST['prodi']
        id_fakultas = ProdiModel.objects.get(id=id_prodi)
        mahasiswa = mahasiswa_form_edit.save(commit=False)
        mahasiswa.fakultas  = id_fakultas.fakultas
        mahasiswa.save()
        messages.info(request, 'Data Mahasiswa Berhasil di Edit')
        return redirect('master_mahasiswa_backend')
    else :
        print(mahasiswa_form_edit.errors)

    context = {
        'form_edit' : mahasiswa_form_edit,
        'action' : 'update',
    }
    return render(request, "landingpage/backend/master_mahasiswa_backend.html", context)

def master_mahasiswa_backend_delete(request, id):
    MahasiswaModel.objects.filter(id=id).delete()
    messages.error(request, 'Data Mahasiswa Berhasil di Hapus')
    return redirect('master_mahasiswa_backend')


#>>>>>>>>>>>>>>>>>> Backend Views <<<<<<<<<<<<<<#
def contact_backend (request):
    contact_update = ContactModel.objects.get(id='1')
    data = {
        'no_hp' : contact_update.no_hp,
        'email' : contact_update.email,
        'ig'    : contact_update.ig,
        'alamat': contact_update.alamat,
    }
    contact_form = ContactForm(request.POST or None, request.FILES or None, initial=data, instance=contact_update)
    
    if request.method == 'POST' :
        if contact_form.is_valid():
            contact_form.save()
            messages.info(request, 'Data Contact Berhasil di Edit')
            
    context = {
        'data':contact_update,
        'form':contact_form,
    }
    return render(request,'landingpage/backend/contact_backend.html', context)

def event_backend (request):
    data = EventModel.objects.get(id='1')
    event_form = EventForm(request.POST, request.FILES or None, instance=data)
    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'event_form' in result_request
        if cek_image == False:
            if data.event_image:
                if os.path.isfile(data.event_image.path) == True:
                    os.remove(data.event_image.path)
        if event_form.is_valid():
            event_form.save()
            event_form = EventForm(instance = data)
            messages.info(request, 'Data Event Berhasil di Edit')
            return redirect('event_backend')
    context = {
        'form': event_form,
        'data': data,
    }
    return render(request, 'landingpage/backend/event_backend.html', context)

def textbooks_backend_delete(request, id):
    TextBooksModel.objects.filter(id=id).delete()
    messages.error(request, 'Data Text Books Berhasil di Hapus')
    return redirect('textbooks_backend')

def textbooks_backend_update (request, id):
    textbooks_edit = TextBooksModel.objects.get(id=id)

    data_edit = {
        'nidn' : textbooks_edit.nidn,
        'nama_dosen' : textbooks_edit.nama_dosen,
        'program_studi' : textbooks_edit.program_studi,
        'fakultas' : textbooks_edit.fakultas,
        'judul_buku' : textbooks_edit.judul_buku,
        'tahap_luaran_10' : textbooks_edit.tahap_luaran_10,
        'tahap_luaran_40' : textbooks_edit.tahap_luaran_40,
        'tahap_luaran_80' : textbooks_edit.tahap_luaran_80,
        'reviewer' : textbooks_edit.reviewer,
        'tahun' : textbooks_edit.tahun,
        'link' : textbooks_edit.link,
    }
    textbooks_form_edit = TextBookForm(request.POST or None, initial=data_edit, instance=textbooks_edit) 

    if request.method == "POST" and textbooks_form_edit.is_valid():
        textbooks_form_edit.save()
        messages.info(request, 'Data Text Books Berhasil di Edit')
        return redirect('textbooks_backend')
    else :
        print(textbooks_form_edit.errors)

    context = {
        'form' : textbooks_form_edit,
    }
    return render(request, 'landingpage/backend/textbooks_backend_update.html', context)

def divisippi_backend (request):
    divisippi_update = DivisiModel.objects.get(id='1')
    data = {
        'members_divisi' : divisippi_update.members_divisi,
        'overview_divisi' : divisippi_update.overview_divisi,
    }
    divisippi_form = DivisiForm(request.POST or None, request.FILES or None, initial=data, instance=divisippi_update)

    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'members_divisi' in result_request
        if cek_image == False:
            if divisippi_update.members_divisi:
                if os.path.isfile(divisippi_update.members_divisi.path) == True:
                    os.remove(divisippi_update.members_divisi.path)
        if divisippi_form.is_valid():
            divisippi_form.save()
            messages.info(request, 'Data Divisi E-learning Berhasil di Edit')
            return redirect('divisippi_backend')
        else:
            print(divisippi_form.errors)

    context = {
        'form': divisippi_form,
        'data': divisippi_update,
    }
    return render(request, 'landingpage/backend/divisippi_backend.html', context)

def divisielearning_backend (request):
    divisielearning_update = DivisiModel.objects.get(id='2')
    data = {
        'members_divisi' : divisielearning_update.members_divisi,
        'overview_divisi' : divisielearning_update.overview_divisi,
    }
    divisielearning_form = DivisiForm(request.POST or None, request.FILES or None, initial=data, instance=divisielearning_update)

    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'members_divisi' in result_request
        if cek_image == False:
            if divisielearning_update.members_divisi:
                if os.path.isfile(divisielearning_update.members_divisi.path) == True:
                    os.remove(divisielearning_update.members_divisi.path)
        if divisielearning_form.is_valid():
            divisielearning_form.save()
            messages.info(request, 'Data Divisi E-learning Berhasil di Edit')
            return redirect('divisielearning_backend')
        else:
            print(divisielearning_form.errors)

    context = {
        'form': divisielearning_form,
        'data': divisielearning_update,
    }
    return render(request, 'landingpage/backend/divisielearning_backend.html', context)

def articletranslation_backend (request):
    articletranslation_update = ServiceModel.objects.get(id='4')
    data = {
        'flowservice_service' : articletranslation_update.flowservice_service,
        'overview_service' : articletranslation_update.overview_service,
    }
    articletranslation_form = ServiceForm(request.POST or None, request.FILES or None, initial=data, instance=articletranslation_update)

    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'flowservice_service' in result_request
        if cek_image == False:
            if articletranslation_update.flowservice_service:
                if os.path.isfile(articletranslation_update.flowservice_service.path) == True:
                    os.remove(articletranslation_update.flowservice_service.path)
        if articletranslation_form.is_valid():
            articletranslation_form.save()
            messages.info(request, 'Data Article Translations Berhasil di Edit')
            return redirect('articletranslation_backend')
        else:
            print(articletranslation_form.errors)

    context = {
        'form': articletranslation_form,
        'data': articletranslation_update,
    }
    return render(request, 'landingpage/backend/articletranslation_backend.html', context)

def sipena_backend (request):
    sipena_update = ServiceModel.objects.get(id='2')
    data = {
        'flowservice_service' : sipena_update.flowservice_service,
        'overview_service' : sipena_update.overview_service,
    }
    sipena_form = ServiceForm(request.POST or None, request.FILES or None, initial=data, instance=sipena_update)

    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'flowservice_service' in result_request
        if cek_image == False:
            if sipena_update.flowservice_service:
                if os.path.isfile(sipena_update.flowservice_service.path) == True:
                    os.remove(sipena_update.flowservice_service.path)
        if sipena_form.is_valid():
            sipena_form.save()
            messages.info(request, 'Data SIPENA Berhasil di Edit')
            return redirect('sipena_backend')
        else:
            print(sipena_form.errors)

    context = {
        'form': sipena_form,
        'data': sipena_update,
    }
    return render(request, 'landingpage/backend/sipena_backend.html', context)

def umktpress_backend (request):
    umktpress_update = ServiceModel.objects.get(id='3')
    data = {
        'flowservice_service' : umktpress_update.flowservice_service,
        'overview_service' : umktpress_update.overview_service,
    }
    umktpress_form = ServiceForm(request.POST or None, request.FILES or None, initial=data, instance=umktpress_update)

    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'flowservice_service' in result_request
        if cek_image == False:
            if umktpress_update.flowservice_service:
                if os.path.isfile(umktpress_update.flowservice_service.path) == True:
                    os.remove(umktpress_update.flowservice_service.path)
        if umktpress_form.is_valid():
            umktpress_form.save()
            messages.info(request, 'Data UMKT PRESS Berhasil di Edit')
            return redirect('umktpress_backend')
        else:
            print(umktpress_form.errors)

    context = {
        'form': umktpress_form,
        'data': umktpress_update,
    }
    return render(request, 'landingpage/backend/umktpress_backend.html', context)

def elearningsupport_backend (request):
    elearningsupport_update = ServiceModel.objects.get(id='1')
    data = {
        'flowservice_service' : elearningsupport_update.flowservice_service,
        'overview_service' : elearningsupport_update.overview_service,
    }
    elearningsupport_form = ServiceForm(request.POST or None, request.FILES or None, initial=data, instance=elearningsupport_update)

    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'flowservice_service' in result_request
        if cek_image == False:
            if elearningsupport_update.flowservice_service:
                if os.path.isfile(elearningsupport_update.flowservice_service.path) == True:
                    os.remove(elearningsupport_update.flowservice_service.path)
        if elearningsupport_form.is_valid():
            elearningsupport_form.save()
            messages.info(request, 'Data Elearning Support Berhasil di Edit')
            return redirect('elearningsupport_backend')
        else:
            print(elearningsupport_form.errors)

    context = {
        'form': elearningsupport_form,
        'data': elearningsupport_update,
    }
    return render(request, 'landingpage/backend/elearningsupport_backend.html', context)

def journal_serving_backend (request):
    data = JournalUmktModel.objects.all().filter(jenis_journal='serving')
    journalserving_form = JournalUmktForm(request.POST or None, request.FILES or None)
    
    if request.method == "POST" and journalserving_form.is_valid():
        journalserving_form.save()
        messages.success(request, 'Data Journal of Social Serving Berhasil di Tambahkan')
        return redirect('journal_serving_backend')
    else :
        print(journalserving_form.errors)
    context = {
         'form': journalserving_form,
         'Data': data,
     }
    return render(request, 'landingpage/backend/journal_serving_backend.html', context)

def journal_serving_backend_delete(request, id):
    data = get_object_or_404(JournalUmktModel,id=id)
    if os.path.isfile(data.cover_jurnal.path) == True:
        os.remove(data.cover_jurnal.path)
    JournalUmktModel.objects.filter(id=id).delete()
    messages.error(request, 'Data Journal of Social Serving Berhasil di Hapus')
    return redirect('journal_serving_backend' )

def journal_serving_backend_update(request, id):
    journal_serving_edit = JournalUmktModel.objects.get(id=id)

    data_edit = {
        'judul_jurnal' : journal_serving_edit.judul_jurnal,
        'issn' : journal_serving_edit.issn,
        'publication' : journal_serving_edit.publication,
        'index' :journal_serving_edit.index,
        'deskripsi' : journal_serving_edit.deskripsi,
        'cover_jurnal' : journal_serving_edit.cover_jurnal,
        'link_view_jurnal' : journal_serving_edit.link_view_jurnal,
        'link_current_issue' : journal_serving_edit.link_current_issue,
        'link_online_submission' : journal_serving_edit.link_online_submission,
        'link_download_template' : journal_serving_edit.link_download_template,
        'jenis_journal' : journal_serving_edit.jenis_journal,
    }
    journal_serving_form_edit = JournalUmktForm(request.POST or None,request.FILES or None, initial=data_edit , instance=journal_serving_edit)
    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'cover_jurnal' in result_request
        if cek_image == False:
            if journal_serving_edit.cover_jurnal:
                if os.path.isfile(journal_serving_edit.cover_jurnal.path) == True:
                    os.remove(journal_serving_edit.cover_jurnal.path)

    if request.method == "POST" and journal_serving_form_edit.is_valid():
        journal_serving_form_edit.save()
        messages.info(request, 'Data Journal of Social Serving Berhasil di Edit')
        return redirect('journal_serving_backend')
    else:
        print(journal_serving_form_edit.errors)

    context = {
        'form': journal_serving_form_edit,
    }
    return render(request, 'landingpage/backend/journal_serving_backend_update.html', context)

def journal_serving_backend_detail(request,id):
    data = JournalUmktModel.objects.get(id=id)
    context = {
        'data': data,
    }
    return render(request, 'landingpage/backend/journal_serving_backend_detail.html', context)
    
def journal_research_backend (request):
    data = JournalUmktModel.objects.all().filter(jenis_journal='research')
    journalresearch_form = JournalUmktForm(request.POST or None, request.FILES or None)
    
    if request.method == "POST" and journalresearch_form.is_valid():
        journalresearch_form.save()
        messages.success(request, 'Data Journal of Social Research Berhasil di Tambahkan')
        return redirect('journal_research_backend')
    else :
        print(journalresearch_form.errors)
    context = {
         'form': journalresearch_form,
         'Data': data,
     }
    return render(request, 'landingpage/backend/journal_research_backend.html', context)

def journal_research_backend_delete(request, id):
    data = get_object_or_404(JournalUmktModel,id=id)
    
    if os.path.isfile(data.cover_jurnal.path) == True:
        os.remove(data.cover_jurnal.path)
    JournalUmktModel.objects.filter(id=id).delete()
    messages.error(request, 'Data Journal of Social Research Berhasil di Hapus')
    return redirect('journal_research_backend' )

def journal_research_backend_update(request, id):
    journal_research_edit = JournalUmktModel.objects.get(id=id)

    data_edit = {
        'judul_jurnal' : journal_research_edit.judul_jurnal,
        'issn' : journal_research_edit.issn,
        'publication' : journal_research_edit.publication,
        'index' :journal_research_edit.index,
        'deskripsi' : journal_research_edit.deskripsi,
        'cover_jurnal' : journal_research_edit.cover_jurnal,
        'link_view_jurnal' : journal_research_edit.link_view_jurnal,
        'link_current_issue' : journal_research_edit.link_current_issue,
        'link_online_submission' : journal_research_edit.link_online_submission,
        'link_download_template' : journal_research_edit.link_download_template,
        'jenis_journal' : journal_research_edit.jenis_journal,
    }
    journal_research_form_edit = JournalUmktForm(request.POST or None,request.FILES or None, initial=data_edit , instance=journal_research_edit)
    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'cover_jurnal' in result_request
        if cek_image == False:
            if journal_research_edit.cover_jurnal:
                if os.path.isfile(journal_research_edit.cover_jurnal.path) == True:
                    os.remove(journal_research_edit.cover_jurnal.path)

    if request.method == "POST" and journal_research_form_edit.is_valid():
        journal_research_form_edit.save()
        messages.info(request, 'Data Journal of Social Research Berhasil di Edit')
        return redirect('journal_research_backend')
    else:
        print(journal_research_form_edit.errors)

    context = {
        'form': journal_research_form_edit,
    }
    return render(request, 'landingpage/backend/journal_research_backend_update.html', context)

def journal_research_backend_detail(request,id):
    data = JournalUmktModel.objects.get(id=id)
    context = {
        'data': data,
    }
    return render(request, 'landingpage/backend/journal_research_backend_detail.html', context)

def downloads_backend(request):
    download_form = DownloadForm(request.POST or None,request.FILES or None)
    data = DownloadContent.objects.all()
    if request.method == 'POST':
        if download_form.is_valid():
            download_form.save()
            messages.success(request, 'Data Download Berhasil di Tambahkan')
            return redirect('downloads_backend')
        else:
            print(download_form.errors)
    
    context = {
        'form': download_form,
        'Data': data,
    }
    return render(request, 'landingpage/backend/download_backend.html', context)

def downloads_backend_update(request, id):
    download_edit = DownloadContent.objects.get(id=id)

    data_edit = {
        'nama_file' : download_edit.nama_file,
        'jenis_file' : download_edit.jenis_file,
        'ukuran_file' : download_edit.ukuran_file,
        'file_download' :download_edit.file_download,
    }
    download_form_edit = DownloadForm(request.POST or None,request.FILES or None, initial=data_edit , instance=download_edit)
    
    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'file_download' in result_request
        if cek_image == False:
            if download_edit.file_download:
                if os.path.isfile(download_edit.file_download.path) == True:
                    os.remove(download_edit.file_download.path)

    if request.method == "POST" and download_form_edit.is_valid():
        download_form_edit.save()
        messages.info(request, 'Data Download Berhasil di Edit')
        return redirect('downloads_backend')
    else:
        print(download_form_edit.errors)

    context = {
        'form': download_form_edit,
    }
    return render(request, 'landingpage/backend/download_backend_update.html', context)

def downloads_backend_delete(request, id):
    data = get_object_or_404(DownloadContent,id=id)
    
    if os.path.isfile(data.file_download.path) == True:
        os.remove(data.file_download.path)
    DownloadContent.objects.filter(id=id).delete()
    messages.error(request, 'Data Download Berhasil di Hapus')
    return redirect('downloads_backend' )

def news_backend(request):
    news_form = NewsForm(request.POST or None,request.FILES or None)
    data = NewsModel.objects.all()
    user = request.user.id
    created_at = int(round(time.time() * 1000))
    if request.method == 'POST':
        if news_form.is_valid():
            news_form.save()
            messages.success(request, 'Data Berita Berhasil di Tambahkan')
            return redirect('news_backend')
        else:
            print(news_form.errors)
    
    context = {
        'form': news_form,
        'user': user,
        'created_at': created_at,
        # 'Data': data,
    }
    return render(request, 'landingpage/backend/news_backend.html',context)

def status(value):
    val_status = ''
    badge = ''
    if value == '0':
        val_status = 'Belum'
        badge = 'danger'
    elif value == '1':
        val_status = 'Dalam Pengajuan'
        badge = 'primary'
    elif value == '2':
        val_status = 'Sudah'
        badge = 'success'
    
    return val_status, badge

# @login_required(login_url='login')
# @group_required(('admin','staff'), login_url='/403/')
def validasiOpenlearning(request):
    data_prodi = ProdiModel.objects.all()
    form_matkul = matkulForm(request.POST or None)
    form_team_teach = TeamTeachingForm(request.POST or None)
    form_validasi_opl = validasiOplForm(request.POST or None)
    if request.method == "POST":
        if request.is_ajax():
            # print('cek data',request.POST['pemilik_course'])
            if form_matkul.is_valid():
                form_matkul.save()
                data = ValidasiOpl()
                data.kode_matkul = form_matkul.cleaned_data['kode_matkul']
                data.nama_matkul = form_matkul.cleaned_data['nama_matkul']
                data.link_matkul = form_matkul.cleaned_data['link_matkul']
                data.pemilik_course = form_matkul.cleaned_data['pemilik_course']
                data.prodi = form_matkul.cleaned_data['prodi']

                return JsonResponse({
                    'id' : data.id,
                    'kode_matkul' : data.kode_matkul,
                    'nama_matkul' : data.nama_matkul,
                    'link_matkul' : data.link_matkul,
                    'pemilik_course' : data.pemilik_course.nama,
                })
            else:
                print(form_matkul.errors)
    
    context = {
        'data_prodi':data_prodi,
        'form_matkul':form_matkul,
        'form_team_teach':form_team_teach,
        'data_form_validasi_opl':form_validasi_opl,
    }
    

    return render(request, 'landingpage/backend/openlearning_backend.html', context)

def validasi_openlearning_detail(request, id):
    data = get_object_or_404(ValidasiOpl,id=id)
    data_anggota_dosen = TeamTeachingModel.objects.select_related('team_teaching').filter(matkul=id)
    form_team_teaching = TeamTeachingForm(request.POST or None)
    if request.method == 'POST' and form_team_teaching.is_valid():
        # Logic Simpan Penelitian
        id_team_teaching = request.POST['team_teaching']
        if TeamTeachingModel.objects.filter(team_teaching=id_team_teaching,matkul=id).exists():
            messages.error(request, 'Dosen Team Teaching Sudah ada')
            redirect('validasi_openlearning_detail', id)
        elif ValidasiOpl.objects.filter(pemilik_course=id_team_teaching,id=id).exists():
            messages.error(request, 'Dosen Sudah Menjadi Pemilik Course')
            redirect('validasi_openlearning_detail', id)
        else:
            matkul = ValidasiOpl.objects.get(id=id)
            data_dosen = DosenModel.objects.get(id=id_team_teaching)
            matkul_form = form_team_teaching.save(commit=False)
            matkul_form.matkul = matkul
            matkul_form.fakultas = data_dosen.fakultas
            matkul_form.prodi = data_dosen.prodi
            matkul_form.save()
            messages.success(request, 'Dosen Team Teaching Berhasil di Tambahkan')
            redirect('validasi_openlearning_detail', id)
    else:
        print(form_team_teaching.errors)
        
    context = {
        'Data':data,
        'aksi':'detail',
        'form_team_teaching': form_team_teaching,
        'data_anggota_dosen':data_anggota_dosen,
    }
    return render(request, 'landingpage/backend/openlearning_backend_detail.html', context)

def team_teach_delete(request, id):
    data = get_object_or_404(TeamTeachingModel,id=id)
    data.delete()  
    messages.error(request, 'Dosen Team Teaching Berhasil di Hapus')
    return redirect('validasi_openlearning_detail', data.matkul.id) 

# @login_required(login_url='login')
# @group_required(('admin','staff'), login_url='/403/')
def showDataMatkul(request):
    data_validasi_opl = ValidasiOpl.objects.select_related('pemilik_course').all()
    data = []
    for obj in data_validasi_opl:
        statushaki , badge = status(obj.status_haki)
        item = {
            'id' : obj.id,
            'kode_matkul' : obj.kode_matkul,
            'nama_matkul' : obj.nama_matkul,
            'link_matkul' : obj.link_matkul,
            'pemilik_course' : obj.pemilik_course.nama,            
            'progres' : obj.progres,            
            'keterangan' : obj.keterangan,            
            'status_haki' : statushaki,            
            'badge' : badge,            
        }
        data.append(item)
    return JsonResponse({'data' : data})

def show_team_teaching(request, id):
    data_team_teach = TeamTeachingModel.objects.select_related('matkul','team_teaching','prodi').filter(matkul=id)
    data = []
    for obj in data_team_teach:
        item = {
            'id' : obj.id,
            'team_teaching' : obj.team_teaching.nama,
            'prodi' : obj.team_teaching.prodi.nama_prodi,
        }
        data.append(item)
    return JsonResponse({'data' : data})

# @login_required(login_url='login')
# @group_required(('admin','staff'), login_url='/403/')
def filterValidasiMatkul(request , data_filter):
    if data_filter == 'all':
        data_validasi_opl = ValidasiOpl.objects.all()
    else:
        data_validasi_opl = ValidasiOpl.objects.select_related('pemilik_course').filter(prodi = data_filter)
    data = []
    for obj in data_validasi_opl:
        statushaki , badge = status(obj.status_haki)
        item = {
            'id' : obj.id,
            'kode_matkul' : obj.kode_matkul,
            'nama_matkul' : obj.nama_matkul,
            'link_matkul' : obj.link_matkul,
            'pemilik_course' : obj.pemilik_course.nama,         
            'progres' : obj.progres,            
            'keterangan' : obj.keterangan,            
            'status_haki' : statushaki,            
            'badge' : badge,            
        }
        data.append(item)
    return JsonResponse({'data' : data})

# @login_required(login_url='login')
# @group_required(('admin','staff'), login_url='/403/')
def filterDataMatkul(request , data_filter):
    if data_filter == 'all':
        data_validasi_opl = ValidasiOpl.objects.select_related('pemilik_course').all()
    else:
        data_validasi_opl = ValidasiOpl.objects.select_related('pemilik_course').filter(prodi = data_filter)
    data = []
    for obj in data_validasi_opl:
        item = {
            'id' : obj.id,
            'kode_matkul' : obj.kode_matkul,
            'nama_matkul' : obj.nama_matkul,
            'link_matkul' : obj.link_matkul,
            'pemilik_course' : obj.pemilik_course.nama,        
            'progres' : obj.progres,            
            'keterangan' : obj.keterangan,            
            'status_haki' : obj.status_haki,            
        }
        data.append(item)
    return JsonResponse({'data' : data})

# @login_required(login_url='login')
# @group_required(('admin','staff'), login_url='/403/')
def detailDataMatkul(request, id):
    data_matkul = ValidasiOpl.objects.select_related('pemilik_course','prodi').get(id=id)

    data = {
        'id' : id,
        'kode_matkul' : data_matkul.kode_matkul,
        'nama_matkul' : data_matkul.nama_matkul,
        'link_matkul' : data_matkul.link_matkul,
        'pemilik_course' : data_matkul.pemilik_course.id,
        'pemilik_course_nama' : data_matkul.pemilik_course.nama,
        'prodi' : data_matkul.prodi.id,
        'ch1' : data_matkul.ch1,
        'ch2' : data_matkul.ch2,
        'ch3' : data_matkul.ch3,
        'ch4' : data_matkul.ch4,
        'ch5' : data_matkul.ch5,
        'ch6' : data_matkul.ch6,
        'ch7' : data_matkul.ch7, 
        'ch8' : data_matkul.ch8,
        'ch9' : data_matkul.ch9,
        'ch10' : data_matkul.ch10,
        'ch11' : data_matkul.ch11,
        'ch12' : data_matkul.ch12,
        'ch13' : data_matkul.ch13,
        'ch14' : data_matkul.ch14,
        'progres' : data_matkul.progres,
        'keterangan' : data_matkul.keterangan,
        'status_haki' : data_matkul.status_haki,
    }
    return JsonResponse({'dataDetailMatkul': data})

# @login_required(login_url='login')
# @group_required(('admin','staff'), login_url='/403/')
def editDataMatkul(request, id):
    data_matkul_edit =  get_object_or_404(ValidasiOpl,id=id)
    if request.method == "POST" :
        form_matkul = matkulForm(request.POST,instance=data_matkul_edit)
        if form_matkul.is_valid():
            form_matkul.save()
        else:
            print('dataInvalid')

    return JsonResponse({'data': id})

def tambah_team_teach(request, id):
    form_team_teach = TeamTeachingForm(request.POST or None)
    if request.method == "POST" and form_team_teach.is_valid() :
            id_dosen = request.POST['team_teaching']
            matkul = ValidasiOpl.objects.get(id=id)
            data_dosen = DosenModel.objects.get(id=id_dosen)
            form = form_team_teach.save(commit=False)
            form.matkul = matkul
            form.fakultas = data_dosen.fakultas
            form.prodi = data_dosen.prodi
            form.save()
            print('Berhasil -----------------------------------')
    else:
        print('dataInvalid', form_team_teach.errors)

    return JsonResponse({'data': id})


# @login_required(login_url='login')
def hapusDataMatkul(request, id):
    data_matkul_hapus = ValidasiOpl.objects.get(id=id)

    if request.is_ajax() and request.method == "POST":
        data_matkul_hapus.delete()
    
    return JsonResponse({'data_hapus': data_matkul_hapus.nama_matkul})    

def hapus_team_teach(request, id):
    data_team_teach = TeamTeachingModel.objects.select_related('team_teaching').get(id=id)

    if request.is_ajax() and request.method == "POST":
        data_team_teach.delete()
    
    return JsonResponse({'data_hapus': data_team_teach.team_teaching.nama})    

# @login_required(login_url='login')
# @group_required(('admin','staff'), login_url='/403/')
def validasiMatkulOpl(request, id):
    data_validasi_opl = get_object_or_404(ValidasiOpl,id = id)
    form_validasi_opl = validasiOplForm(request.POST, instance = data_validasi_opl)
    progres = request.POST.get('progres')
    if request.is_ajax :
        if form_validasi_opl.is_valid():
            form_validasi_opl.save()
        else:
            pass

    return JsonResponse({'data_validasi': data_validasi_opl.nama_matkul})

def openlearning_dosen(request):
    if request.method == "GET":
        if request.GET.get('dosen'):
            dosen = request.GET.get('dosen')
            data_openlearning = ValidasiOpl.objects.filter(Q(pemilik_course=dosen) | Q(teamteachingmodel__team_teaching=dosen))
        elif request.GET.get('prodi'):
            prodi = request.GET.get('prodi')
            data_openlearning = ValidasiOpl.objects.select_related('prodi').filter(prodi=prodi)
        else:
            data_openlearning = ValidasiOpl.objects.all()
        
        for openlearning in data_openlearning:
            openlearning.progres = int(openlearning.progres)
            openlearning.team_teach = TeamTeachingModel.objects.filter(matkul=openlearning)

    data_prodi = ProdiModel.objects.all()
    context ={
        'data_openlearning': data_openlearning,
        'data_prodi': data_prodi,
    }   
    return render(request, 'landingpage/backend/openlearning_backend_dosen.html',context)