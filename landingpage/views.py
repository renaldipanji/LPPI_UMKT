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

    #>>>>>>>>>>>>>>>> Backend Views <<<<<<<<<<<<<<<<<<<<<

def orgstruktur_backend (request):
    data = orgstruktur.objects.get(id='1')
    orgstruktur_form = OrgstrukturForm(request.FILES, request.POST or None)
    #if request.method == "POST":
        # #result_request = dict(request.POST)
        # print(result_request)
        # #ambil data cek image
        # cek_file = 'file_orgstruktur' in result_request
        # if cek_file == False:
        #     if data :
        #         if os.path.isfile(data.file_orgstruktur.path) == True:
        #             os.remove(data.file_orgstruktur.path)
        # if orgstruktur_form.is
    context = {
        'form': orgstruktur_form,
        'data': data,
    }
    return render(request, 'landingpage/backend/orgstruktur_backend.html', context)

def divisippi_backend (request):
    #data = divisippi.objects.get(id='1')
    # divisippi_form = DivisippiForm(request.FILES, request.POST or None)
    # context = {
    #     'form': divisippi_form,
    #     #'data': data,
    # }
    return render(request, 'landingpage/backend/divisippi_backend.html')

def articletranslation_backend (request):
    #data = divisippi.objects.get(id='1')
    # divisippi_form = DivisippiForm(request.FILES, request.POST or None)
    # context = {
    #     'form': divisippi_form,
    #     #'data': data,
    # }
    return render(request, 'landingpage/backend/articletranslation_backend.html')

def sipena_backend (request):
    #data = divisippi.objects.get(id='1')
    # divisippi_form = DivisippiForm(request.FILES, request.POST or None)
    # context = {
    #     'form': divisippi_form,
    #     #'data': data,
    # }
    return render(request, 'landingpage/backend/sipena_backend.html')

def journalresearch_backend (request):
    #data = divisippi.objects.get(id='1')
    # divisippi_form = DivisippiForm(request.FILES, request.POST or None)
    # context = {
    #     'form': divisippi_form,
    #     #'data': data,
    # }
    return render(request, 'landingpage/backend/journalresearch_backend.html')

def newspaper_backend(request):
    data = NewspaperModel.objects.all()
    newspaper_form = NewspaperForm(request.POST or None)
    if request.method == "POST" and newspaper_form.is_valid():
        newspaper_form.save()
        redirect('newspaper_backend')
    else:
        print(newspaper_form.errors)

    context = {
        'form': newspaper_form,
        'Data': data,
    }
    return render(request, 'landingpage/backend/newspaper_backend.html', context)

def newspaper_backend_delete(request, id):
    NewspaperModel.objects.filter(id=id).delete()
    return redirect('newspaper_backend')

def newspaper_backend_update(request,id):
    newspaper_edit = NewspaperModel.objects.get(id=id)

    data_edit = {
        'nidn' : newspaper_edit.nidn,
        'nama_dosen' : newspaper_edit.nama_dosen,
        'program_studi' : newspaper_edit.program_studi,
        'fakultas' : newspaper_edit.fakultas,
        'judul_artikel' : newspaper_edit.judul_artikel,
        'tahun' : newspaper_edit.tahun,
        'link' : newspaper_edit.link,
    }
    newspaper_form_edit = NewspaperForm(request.POST or None, initial=data_edit , instance=newspaper_edit)

    if request.method == "POST" and newspaper_form_edit.is_valid():
        newspaper_form_edit.save()
        return redirect('newspaper_backend')
    else:
        print(newspaper_form_edit.errors)

    context = {
        'form': newspaper_form_edit,
    }

    return render(request, 'landingpage/backend/newspaper_backend_update.html', context)