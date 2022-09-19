from django.shortcuts import render

# Create your views here.
def visi_misi(request):
    return render(request,'landingpage/visi_misi.html')

def about(request):
    return render(request, 'landingpage/about.html')

def contact(request):
    return render(request, 'landingpage/contact.html')