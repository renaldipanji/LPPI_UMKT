from django.shortcuts import render

# Create your views here.
def visi_misi(request):
    return render(request,'landingpage/visi_misi.html')

def about(request):
    return render(request, 'landingpage/about.html')

def journal(request):
    return render(request, 'landingpage/journal.html')

def newspaper(request):
    return render(request, 'landingpage/newspaper.html')

def textbook(request):
    return render(request, 'landingpage/textbook.html')

def downloads(request):
    return render(request, 'landingpage/downloads.html')
    