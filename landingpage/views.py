from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
def about(request):
    return render(request,'landingpage/frontend/about.html')

def visi_misi(request):
    return render(request,'landingpage/frontend/visi_misi.html')
    
def index(request):
    return render(request,'landingpage/frontend/index.html')

def org_struktur(request):
    return render(request,'landingpage/frontend/org_struktur.html')

def devisi(request):
    return render(request,'landingpage/frontend/devisi.html')

def contact(request):
    return render(request, 'landingpage/frontend/contact.html')

def workprog(request):
    return render(request,'landingpage/frontend/workprog.html')

def divisi_ppi(request):
    return render(request,'landingpage/frontend/divisi_ppi.html')

def divisi_elearning(request):
    return render(request, 'landingpage/frontend/divisi_elearning.html')

def news(request):
    return render(request, 'landingpage/frontend/news.html')

def news_single(request):
    return render(request, 'landingpage/frontend/news_single.html')

def event(request):
    return render(request, 'landingpage/frontend/event.html')
    
def journal(request):
    return render(request, 'landingpage/frontend/journal.html')

def newspaper(request):
    return render(request, 'landingpage/frontend/newspaper.html')

def textbook(request):
    return render(request, 'landingpage/frontend/textbook.html')

def downloads(request):
    return render(request, 'landingpage/frontend/downloads.html')

def journal_research_umkt(request):
    return render(request, 'landingpage/frontend/jurnal_penelitian_umkt.html')

def journal_social_umkt(request):
    return render(request, 'landingpage/frontend/jurnal_pengabdian_umkt.html')

def translate_art(request):
    return render(request, 'landingpage/frontend/translate_art.html')

def sipena(request):
    return render(request, 'landingpage/frontend/sipena.html')

def umktpress(request):
    return render(request, 'landingpage/frontend/umktpress.html')

def e_learning(request):
    return render(request, 'landingpage/frontend/e_learning.html')

#>>>>>>>>>>>>BACKEND<<<<<<<<<<<<<
def workprogramme_backend (request):
    data = Workprogramme.objects.get(id='1')
    workprogramme_form = WorkprogrammeForm(request.FILES, request.POST or None,instance = data)
    if request.method == "POST":
            result_request = dict(request.POST)
            print(result_request)
            # ambil data cek image
            # cek_file = 'file_workprogramme' in result_request
            # if cek_file == False:
            #     if data :
            #         if os.path.isfile(data.file_workprogramme.path) == True:
            #             os.remove(data.file_workprogramme.path)
            # if workprogramme_form.is_valid():
            #     workprogramme_form.save()
            #     formFoto = WorkprogrammeForm(instance = data)
            #     # messages.success(request, 'Data Work Programme Berhasil di Update')
            #     return redirect('workprogramme_backend')
            # else:
            #     print(workprogramme_form.errors)
    context = {
        'form' : workprogramme_form,
        'data' : data,
    }
    return render(request, 'landingpage/backend/workprogramme_backend.html', context)

def visimisi_backend (request):
    #data = Visimisi.objects.get(id='1')
    # visi_form = VisimisiForm(request.FILES, request.POST or None)
    # if request.method == "POST":
    #         result_request = dict(request.POST)
    #         print(result_request)
    # context = {
    #     'form' : visimisi_form,
    #     #'data' : data,
    # }
    return render(request, 'landingpage/backend/visimisi_backend.html')

def journals_backend (request):
    data = JournalsModel.objects.all()
    journals_form = JournalsForm(request.POST or None)
    if request.method == "POST" and journals_form.is_valid():
        journals_form.save()
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
        redirect('textbooks_backend')
    else :
        print(textbooks_form.errors)

    context = {
        'form' : textbooks_form,
        'Data' : data,
    }
    return render(request, 'landingpage/backend/textbooks_backend.html', context)

def textbooks_backend_delete(request, id):
    TextBooksModel.objects.filter(id=id).delete()
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
        return redirect('textbooks_backend')
    else :
        print(textbooks_form_edit.errors)

    context = {
        'form' : textbooks_form_edit,
    }
    return render(request, 'landingpage/backend/textbooks_backend_update.html', context)




