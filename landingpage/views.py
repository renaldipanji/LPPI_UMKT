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