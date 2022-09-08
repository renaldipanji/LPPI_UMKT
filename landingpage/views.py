from django.shortcuts import render

# Create your views here.
def visi_misi(request):
    return render(request,'landingpage/visi_misi.html')