from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def about(request):
    return render(request,'landingpage/about.html')

def visi_misi(request):
    return render(request,'landingpage/visi_misi.html')
    
def index(request):
    return render(request,'landingpage/index.html')

def org_struktur(request):
    return render(request,'landingpage/org_struktur.html')

def devisi(request):
    return render(request,'landingpage/devisi.html')

def contact(request):
    return render(request, 'landingpage/contact.html')

def workprog(request):
    return render(request,'landingpage/workprog.html')

def divisi_ppi(request):
    return render(request,'landingpage/divisi_ppi.html')

def divisi_elearning(request):
    return render(request, 'landingpage/divisi_elearning.html')

def news(request):
    return render(request, 'landingpage/news.html')

def news_single(request):
    return render(request, 'landingpage/news_single.html')

def event(request):
    return render(request, 'landingpage/event.html')
    
def journal(request):
    return render(request, 'landingpage/journal.html')

def newspaper(request):
    return render(request, 'landingpage/newspaper.html')

def textbook(request):
    return render(request, 'landingpage/textbook.html')

def downloads(request):
    return render(request, 'landingpage/downloads.html')

def journal_research_umkt(request):
    return render(request, 'landingpage/jurnal_penelitian_umkt.html')

def journal_social_umkt(request):
    return render(request, 'landingpage/jurnal_pengabdian_umkt.html')

def translate_art(request):
    return render(request, 'landingpage/translate_art.html')

def sipena(request):
    return render(request, 'landingpage/sipena.html')

def umktpress(request):
    return render(request, 'landingpage/umktpress.html')

def e_learning(request):
    return render(request, 'landingpage/e_learning.html')

#>>>>>>>>>>>>>>>>>> Backend Views <<<<<<<<<<<<<<#

def contact_backend (request):
    #data = divisippi.objects.get(id='1')
   # divisippi_form = DivisippiForm(request.FILES, request.POST or None)
   # context = {
   #     'form': divisippi_form,
   #     #'data': data,
   # }
   return render(request, 'landingpage/backend/contact_backend.html')

def umkt_press_backend (request):
    #data = divisippi.objects.get(id='1')
   # divisippi_form = DivisippiForm(request.FILES, request.POST or None)
   # context = {
   #     'form': divisippi_form,
   #     #'data': data,
   # }
   return render(request, 'landingpage/backend/umkt_press_backend.html')

def elearning_support_backend (request):
    elearning_support_update = ElearningSupport.objects.get(id='1')
    data = {
        'elearningsupport_flowservice' : elearning_support_update.elearningsupport_flowservice,
        'elearningsupport_overview' : elearning_support_update.elearningsupport_overview,
    }
    elearning_support_form = ElearningsupportForm(request.POST or None, request.FILES or None, initial=data, instance=elearning_support_update)
    
    if request.method == 'POST' :
        if elearning_support_form.is_valid():
            elearning_support_form.save()
            
    context = {
        'data':elearning_support_update,
        'form':elearning_support_form,
    }
    return render(request, 'landingpage/backend/elearning_support_backend.html', context)