from django.shortcuts import render
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
    data = OrgstrukturModel.objects.get(id='2')
    context ={
        'data': data,
    }
    return render(request,'landingpage/frontend/org_struktur.html', context)

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
    orgstruktur_update = OrgstrukturModel.objects.get(id='2')
    data = {
        'orgstruktur_image' : orgstruktur_update.orgstruktur_image,
    }
    orgstruktur_form = OrgstrukturForm(request.POST or None, request.FILES  or None, initial=data, instance=orgstruktur_update)

    if request.method == 'POST':
        result_request = dict(request.POST)
        print(result_request)
        #ambil data cek image
        cek_image = 'orgstruktur_image' in result_request
        if cek_image == False:
            if orgstruktur_update.orgstruktur_image:
                if os.path.isfile(orgstruktur_update.orgstruktur_image.path) == True:
                    os.remove(orgstruktur_update.orgstruktur_image.path)
        if orgstruktur_form.is_valid():
            orgstruktur_form.save()
            # messages.success(request, 'Foto Berhasil di Edit')
            return redirect('orgstruktur_backend')
    context = {
        'form': orgstruktur_form,
        'data': orgstruktur_update,
    }
    return render(request, 'landingpage/backend/orgstruktur_backend.html', context)