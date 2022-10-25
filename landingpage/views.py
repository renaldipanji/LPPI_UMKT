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

def journal_serving_backend (request):
    data = JournalServingModel.objects.all()
    journalserving_form = JournalServingForm(request.POST or None, request.FILES or None)
    
    if request.method == "POST" and journalserving_form.is_valid():
        journalserving_form.save()
        redirect('journal_serving_backend')
    else :
        print(journalserving_form.errors)
    context = {
         'form': journalserving_form,
         'Data': data,
     }
    return render(request, 'landingpage/backend/journal_serving_backend.html', context)

def journal_serving_backend_delete(request, id):
    data = get_object_or_404(JournalServingModel,id=id)
    
    if os.path.isfile(data.cover_jurnal.path) == True:
        os.remove(data.cover_jurnal.path)
    JournalServingModel.objects.filter(id=id).delete()
    return redirect('journal_serving_backend' )

def journal_serving_backend_update(request, id):
    journal_serving_edit = JournalServingModel.objects.get(id=id)

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
    }
    journal_serving_form_edit = JournalServingForm(request.POST or None,request.FILES or None, initial=data_edit , instance=journal_serving_edit)
    
    if request.method == "POST" and journal_serving_form_edit.is_valid():
        journal_serving_form_edit.save()
        return redirect('journal_serving_backend')
    else:
        print(journal_serving_form_edit.errors)

    context = {
        'form': journal_serving_form_edit,
    }
    return render(request, 'landingpage/backend/journal_serving_backend_update.html', context)
