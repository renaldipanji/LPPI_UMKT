from django.shortcuts import render

# Create your views here.
def visi_misi(request):
    return render(request,'landingpage/visi_misi.html')

def workprog(request):
    return render(request,'landingpage/workprog.html')

def divisi_ppi(request):
    return render(request,'landingpage/divisi_ppi.html')

def divisi_elearning(request):
    return render(request, 'landingpage/divisi_elearning.html')

def event(request):
    return render(request, 'landingpage/event.html')