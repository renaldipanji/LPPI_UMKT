from django.shortcuts import render

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
    
