from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

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
    return render(request,'landingpage/frontend/divisi_ppi.html')

def divisi_elearning(request):
    return render(request, 'landingpage/frontend/divisi_elearning.html')

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
        #ambil data cek image
        cek_image = 'orgstruktur_image' in result_request
        if cek_image == False:
            if orgstruktur_update.orgstruktur_image:
                if os.path.isfile(orgstruktur_update.orgstruktur_image.path) == True:
                    os.remove(orgstruktur_update.orgstruktur_image.path)
        if orgstruktur_form.is_valid():
            orgstruktur_form.save()
            messages.success(request, 'Data Struktur Organisasi Berhasil di Edit')
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
            messages.success(request, 'Data Visi Misi Berhasil di Edit')
    context = {
        'form' : visimisi_form,
        'data' : visimisi_update,
    }
    return render(request, 'landingpage/backend/visimisi_backend.html', context)

def journals_backend (request):
    #data = Visimisi.objects.get(id='1')
    journals_form = JournalsForm(request.FILES, request.POST or None)
    # if request.method == "POST":
    #         result_request = dict(request.POST)
    #         print(result_request)
    context = {
        'form' : journals_form,
    #     #'data' : data,
    }
    return render(request, 'landingpage/backend/journals_backend.html', context)

def textbooks_backend (request):
    #data = Visimisi.objects.get(id='1')
    textbooks_form = TextBookForm(request.POST, request.FILES or None)
    # if request.method == "POST":
    #         result_request = dict(request.POST)
    #         print(result_request)
    context = {
        'form' : textbooks_form,
        #'data' : data,
    }
    return render(request, 'landingpage/backend/textbooks_backend.html', context)
    return render(request, 'landingpage/e_learning.html')

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
            messages.success(request, 'Data Contact Berhasil di Edit')
            
    context = {
        'data':contact_update,
        'form':contact_form,
    }
    return render(request,'landingpage/backend/contact_backend.html', context)

def journal_serving_backend (request):
    #data = divisippi.objects.get(id='1')
   # divisippi_form = DivisippiForm(request.FILES, request.POST or None)
   # context = {
   #     'form': divisippi_form,
   #     #'data': data,
   # }
   return render(request, 'landingpage/backend/journal_serving_backend.html')

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
            messages.success(request, 'Data Event Berhasil di Edit')
            return redirect('event_backend')
    context = {
        'form': event_form,
        'data': data,
    }
    return render(request, 'landingpage/backend/event_backend.html', context)
