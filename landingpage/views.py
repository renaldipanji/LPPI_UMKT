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
    data = PPIModel.objects.get(id='1')
    context ={
        'data': data,
    }
    return render(request,'landingpage/frontend/divisi_ppi.html',context)

def divisi_elearning(request):
    data = ElearningModel.objects.get(id='1')
    context ={
        'data': data,
    }
    return render(request, 'landingpage/frontend/divisi_elearning.html',context)

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
    data = JournalsModel.objects.all()
    context ={
        'data_journal': data,
    }   
    return render(request, 'landingpage/frontend/journal.html',context)

def newspaper(request):
    return render(request, 'landingpage/frontend/newspaper.html')

def textbook(request):
    data = TextBooksModel.objects.all()
    context ={
        'data_textbook': data,
    }    
    return render(request, 'landingpage/frontend/textbook.html',context)

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
            messages.info(request, 'Data Struktur Organisasi Berhasil di Edit')
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
            messages.info(request, 'Data Visi Misi Berhasil di Edit')
    context = {
        'form' : visimisi_form,
        'data' : visimisi_update,
    }
    return render(request, 'landingpage/backend/visimisi_backend.html', context)

def journals_backend (request):
    data = JournalsModel.objects.all()
    journals_form = JournalsForm(request.POST or None)
    if request.method == "POST" and journals_form.is_valid():
        journals_form.save()
        messages.info(request, 'Data Journals Berhasil di Edit')
        redirect('journals_backend')
    else :
        print(journals_form.errors)

    context = {
        'form' : journals_form,
        'Data' : data,
    }
    return render(request, 'landingpage/backend/journals_backend.html', context)

def journals_backend_delete(request, id):
    JournalsModel.objects.filter(id=id).delete()
    messages.error(request, 'Data Journals Berhasil di Hapus')
    return redirect('journals_backend')

def journals_backend_update (request, id):
    journals_edit = JournalsModel.objects.get(id=id)

    data_edit = {
        'nidn' : journals_edit.nidn,
        'nama_dosen' : journals_edit.nama_dosen,
        'program_studi' : journals_edit.program_studi,
        'fakultas' : journals_edit.fakultas,
        'judul_artikel' : journals_edit.judul_artikel,
        'tahun' : journals_edit.tahun,
        'link' : journals_edit.link,
    }
    journals_form_edit = JournalsForm(request.POST or None, initial=data_edit, instance=journals_edit) 

    if request.method == "POST" and journals_form_edit.is_valid():
        journals_form_edit.save()
        messages.info(request, 'Data Text Books Berhasil di Edit')
        return redirect('journals_backend')
    else :
        print(journals_form_edit.errors)

    context = {
        'form' : journals_form_edit,
    }

    return render(request, 'landingpage/backend/journals_backend_update.html', context)

def textbooks_backend (request):
    data = TextBooksModel.objects.all()
    textbooks_form = TextBookForm(request.POST or None)
    if request.method == "POST" and textbooks_form.is_valid():
        textbooks_form.save()
        messages.success(request, 'Data Text Books Berhasil di Tambahkan')
        redirect('textbooks_backend')
    else :
        print(textbooks_form.errors)

    context = {
        'form' : textbooks_form,
        'Data' : data,
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
            messages.info(request, 'Data Contact Berhasil di Edit')
            
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
            messages.info(request, 'Data Event Berhasil di Edit')
            return redirect('event_backend')
    context = {
        'form': event_form,
        'data': data,
    }
    return render(request, 'landingpage/backend/event_backend.html', context)

def textbooks_backend_delete(request, id):
    TextBooksModel.objects.filter(id=id).delete()
    messages.error(request, 'Data Text Books Berhasil di Hapus')
    return redirect('textbooks_backend')

def textbooks_backend_update (request, id):
    textbooks_edit = TextBooksModel.objects.get(id=id)

    data_edit = {
        'nidn' : textbooks_edit.nidn,
        'nama_dosen' : textbooks_edit.nama_dosen,
        'program_studi' : textbooks_edit.program_studi,
        'fakultas' : textbooks_edit.fakultas,
        'judul_buku' : textbooks_edit.judul_buku,
        'tahap_luaran_10' : textbooks_edit.tahap_luaran_10,
        'tahap_luaran_40' : textbooks_edit.tahap_luaran_40,
        'tahap_luaran_80' : textbooks_edit.tahap_luaran_80,
        'reviewer' : textbooks_edit.reviewer,
        'tahun' : textbooks_edit.tahun,
        'link' : textbooks_edit.link,
    }
    textbooks_form_edit = TextBookForm(request.POST or None, initial=data_edit, instance=textbooks_edit) 

    if request.method == "POST" and textbooks_form_edit.is_valid():
        textbooks_form_edit.save()
        messages.info(request, 'Data Text Books Berhasil di Edit')
        return redirect('textbooks_backend')
    else :
        print(textbooks_form_edit.errors)

    context = {
        'form' : textbooks_form_edit,
    }
    return render(request, 'landingpage/backend/textbooks_backend_update.html', context)

def divisippi_backend (request):
    divisippi_update = PPIModel.objects.get(id='1')
    data = {
        'flowservice_divisippi' : divisippi_update.flowservice_divisippi,
        'overview_divisippi' : divisippi_update.overview_divisippi,
    }
    divisippi_form = DivisippiForm(request.POST or None, request.FILES or None, initial=data, instance=divisippi_update)

    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'flowservice_divisippi' in result_request
        if cek_image == False:
            if divisippi_update.flowservice_divisippi:
                if os.path.isfile(divisippi_update.flowservice_divisippi.path) == True:
                    os.remove(divisippi_update.flowservice_divisippi.path)
        if divisippi_form.is_valid():
            divisippi_form.save()
            # messages.success(request, 'Foto Berhasil di Edit')
            return redirect('divisippi_backend')
        else:
            print(divisippi_form.errors)

    context = {
        'form': divisippi_form,
        'data': divisippi_update,
    }
    return render(request, 'landingpage/backend/divisippi_backend.html', context)

def divisielearning_backend (request):
    divisielearning_update = ElearningModel.objects.get(id='1')
    data = {
        'flowservice_divisielearning' : divisielearning_update.flowservice_divisielearning,
        'overview_divisielearning' : divisielearning_update.overview_divisielearning,
    }
    divisielearning_form = DivisielearningForm(request.POST or None, request.FILES or None, initial=data, instance=divisielearning_update)

    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'flowservice_divisielearning' in result_request
        if cek_image == False:
            if divisielearning_update.flowservice_divisielearning:
                if os.path.isfile(divisielearning_update.flowservice_divisielearning.path) == True:
                    os.remove(divisielearning_update.flowservice_divisielearning.path)
        if divisielearning_form.is_valid():
            divisielearning_form.save()
            # messages.success(request, 'Foto Berhasil di Edit')
            return redirect('divisielearning_backend')
        else:
            print(divisielearning_form.errors)

    context = {
        'form': divisielearning_form,
        'data': divisielearning_update,
    }
    return render(request, 'landingpage/backend/divisielearning_backend.html', context)

def articletranslation_backend (request):
    articletranslation_update = ServiceModel.objects.get(id='4')
    data = {
        'flowservice_service' : articletranslation_update.flowservice_service,
        'overview_service' : articletranslation_update.overview_service,
    }
    articletranslation_form = ServiceForm(request.POST or None, request.FILES or None, initial=data, instance=articletranslation_update)

    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'flowservice_service' in result_request
        if cek_image == False:
            if articletranslation_update.flowservice_service:
                if os.path.isfile(articletranslation_update.flowservice_service.path) == True:
                    os.remove(articletranslation_update.flowservice_service.path)
        if articletranslation_form.is_valid():
            articletranslation_form.save()
            messages.info(request, 'Data Article Translations Berhasil di Edit')
            return redirect('articletranslation_backend')
        else:
            print(articletranslation_form.errors)

    context = {
        'form': articletranslation_form,
        'data': articletranslation_update,
    }
    return render(request, 'landingpage/backend/articletranslation_backend.html', context)

def sipena_backend (request):
    sipena_update = ServiceModel.objects.get(id='2')
    data = {
        'flowservice_service' : sipena_update.flowservice_service,
        'overview_service' : sipena_update.overview_service,
    }
    sipena_form = ServiceForm(request.POST or None, request.FILES or None, initial=data, instance=sipena_update)

    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'flowservice_service' in result_request
        if cek_image == False:
            if sipena_update.flowservice_service:
                if os.path.isfile(sipena_update.flowservice_service.path) == True:
                    os.remove(sipena_update.flowservice_service.path)
        if sipena_form.is_valid():
            sipena_form.save()
            messages.info(request, 'Data SIPENA Berhasil di Edit')
            return redirect('sipena_backend')
        else:
            print(sipena_form.errors)

    context = {
        'form': sipena_form,
        'data': sipena_update,
    }
    return render(request, 'landingpage/backend/sipena_backend.html', context)

def umktpress_backend (request):
    umktpress_update = ServiceModel.objects.get(id='3')
    data = {
        'flowservice_service' : umktpress_update.flowservice_service,
        'overview_service' : umktpress_update.overview_service,
    }
    umktpress_form = ServiceForm(request.POST or None, request.FILES or None, initial=data, instance=umktpress_update)

    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'flowservice_service' in result_request
        if cek_image == False:
            if umktpress_update.flowservice_service:
                if os.path.isfile(umktpress_update.flowservice_service.path) == True:
                    os.remove(umktpress_update.flowservice_service.path)
        if umktpress_form.is_valid():
            umktpress_form.save()
            messages.info(request, 'Data UMKT PRESS Berhasil di Edit')
            return redirect('umktpress_backend')
        else:
            print(umktpress_form.errors)

    context = {
        'form': umktpress_form,
        'data': umktpress_update,
    }
    return render(request, 'landingpage/backend/umktpress_backend.html', context)

def elearningsupport_backend (request):
    elearningsupport_update = ServiceModel.objects.get(id='1')
    data = {
        'flowservice_service' : elearningsupport_update.flowservice_service,
        'overview_service' : elearningsupport_update.overview_service,
    }
    elearningsupport_form = ServiceForm(request.POST or None, request.FILES or None, initial=data, instance=elearningsupport_update)

    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'flowservice_service' in result_request
        if cek_image == False:
            if elearningsupport_update.flowservice_service:
                if os.path.isfile(elearningsupport_update.flowservice_service.path) == True:
                    os.remove(elearningsupport_update.flowservice_service.path)
        if elearningsupport_form.is_valid():
            elearningsupport_form.save()
            messages.info(request, 'Data Elearning Support Berhasil di Edit')
            return redirect('elearningsupport_backend')
        else:
            print(elearningsupport_form.errors)

    context = {
        'form': elearningsupport_form,
        'data': elearningsupport_update,
    }
    return render(request, 'landingpage/backend/elearningsupport_backend.html', context)