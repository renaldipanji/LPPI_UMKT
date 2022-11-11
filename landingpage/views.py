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
    data = DivisiModel.objects.get(id='1')
    context ={
        'data': data,
    }
    return render(request,'landingpage/frontend/divisi_ppi.html',context)

def divisi_elearning(request):
    data = DivisiModel.objects.get(id='2')
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
    data = DownloadContent.objects.all()
    context={
        'data_downloads':data,
    }
    return render(request, 'landingpage/frontend/downloads.html',context)

def journal_research_umkt(request):
    data = JournalUmktModel.objects.all().filter(jenis_journal='research')
    context ={
        'data_journal' : data,
    }
    return render(request, 'landingpage/frontend/jurnal_penelitian_umkt.html', context)

def journal_social_umkt(request):
    data = JournalUmktModel.objects.all().filter(jenis_journal='serving')
    context ={
        'data_journal' : data,
    }
    return render(request, 'landingpage/frontend/jurnal_pengabdian_umkt.html',context)

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
    divisippi_update = DivisiModel.objects.get(id='1')
    data = {
        'members_divisi' : divisippi_update.members_divisi,
        'overview_divisi' : divisippi_update.overview_divisi,
    }
    divisippi_form = DivisiForm(request.POST or None, request.FILES or None, initial=data, instance=divisippi_update)

    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'members_divisi' in result_request
        if cek_image == False:
            if divisippi_update.members_divisi:
                if os.path.isfile(divisippi_update.members_divisi.path) == True:
                    os.remove(divisippi_update.members_divisi.path)
        if divisippi_form.is_valid():
            divisippi_form.save()
            messages.info(request, 'Data Divisi E-learning Berhasil di Edit')
            return redirect('divisippi_backend')
        else:
            print(divisippi_form.errors)

    context = {
        'form': divisippi_form,
        'data': divisippi_update,
    }
    return render(request, 'landingpage/backend/divisippi_backend.html', context)

def divisielearning_backend (request):
    divisielearning_update = DivisiModel.objects.get(id='2')
    data = {
        'members_divisi' : divisielearning_update.members_divisi,
        'overview_divisi' : divisielearning_update.overview_divisi,
    }
    divisielearning_form = DivisiForm(request.POST or None, request.FILES or None, initial=data, instance=divisielearning_update)

    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'members_divisi' in result_request
        if cek_image == False:
            if divisielearning_update.members_divisi:
                if os.path.isfile(divisielearning_update.members_divisi.path) == True:
                    os.remove(divisielearning_update.members_divisi.path)
        if divisielearning_form.is_valid():
            divisielearning_form.save()
            messages.info(request, 'Data Divisi E-learning Berhasil di Edit')
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

def journal_serving_backend (request):
    data = JournalUmktModel.objects.all().filter(jenis_journal='serving')
    journalserving_form = JournalUmktForm(request.POST or None, request.FILES or None)
    
    if request.method == "POST" and journalserving_form.is_valid():
        journalserving_form.save()
        messages.success(request, 'Data Journal of Social Serving Berhasil di Tambahkan')
        return redirect('journal_serving_backend')
    else :
        print(journalserving_form.errors)
    context = {
         'form': journalserving_form,
         'Data': data,
     }
    return render(request, 'landingpage/backend/journal_serving_backend.html', context)

def journal_serving_backend_delete(request, id):
    data = get_object_or_404(JournalUmktModel,id=id)
    
    if os.path.isfile(data.cover_jurnal.path) == True:
        os.remove(data.cover_jurnal.path)
    JournalUmktModel.objects.filter(id=id).delete()
    messages.error(request, 'Data Journal of Social Serving Berhasil di Hapus')
    return redirect('journal_serving_backend' )

def journal_serving_backend_update(request, id):
    journal_serving_edit = JournalUmktModel.objects.get(id=id)

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
        'jenis_journal' : journal_serving_edit.jenis_journal,
    }
    journal_serving_form_edit = JournalUmktForm(request.POST or None,request.FILES or None, initial=data_edit , instance=journal_serving_edit)
    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'cover_jurnal' in result_request
        if cek_image == False:
            if journal_serving_edit.cover_jurnal:
                if os.path.isfile(journal_serving_edit.cover_jurnal.path) == True:
                    os.remove(journal_serving_edit.cover_jurnal.path)

    if request.method == "POST" and journal_serving_form_edit.is_valid():
        journal_serving_form_edit.save()
        messages.info(request, 'Data Journal of Social Serving Berhasil di Edit')
        return redirect('journal_serving_backend')
    else:
        print(journal_serving_form_edit.errors)

    context = {
        'form': journal_serving_form_edit,
    }
    return render(request, 'landingpage/backend/journal_serving_backend_update.html', context)

def journal_serving_backend_detail(request,id):
    data = JournalUmktModel.objects.get(id=id)
    context = {
        'data': data,
    }
    return render(request, 'landingpage/backend/journal_serving_backend_detail.html', context)
    
def journal_research_backend (request):
    data = JournalUmktModel.objects.all().filter(jenis_journal='research')
    journalresearch_form = JournalUmktForm(request.POST or None, request.FILES or None)
    
    if request.method == "POST" and journalresearch_form.is_valid():
        journalresearch_form.save()
        messages.success(request, 'Data Journal of Social Research Berhasil di Tambahkan')
        return redirect('journal_research_backend')
    else :
        print(journalresearch_form.errors)
    context = {
         'form': journalresearch_form,
         'Data': data,
     }
    return render(request, 'landingpage/backend/journal_research_backend.html', context)

def journal_research_backend_delete(request, id):
    data = get_object_or_404(JournalUmktModel,id=id)
    
    if os.path.isfile(data.cover_jurnal.path) == True:
        os.remove(data.cover_jurnal.path)
    JournalUmktModel.objects.filter(id=id).delete()
    messages.error(request, 'Data Journal of Social Research Berhasil di Hapus')
    return redirect('journal_research_backend' )

def journal_research_backend_update(request, id):
    journal_research_edit = JournalUmktModel.objects.get(id=id)

    data_edit = {
        'judul_jurnal' : journal_research_edit.judul_jurnal,
        'issn' : journal_research_edit.issn,
        'publication' : journal_research_edit.publication,
        'index' :journal_research_edit.index,
        'deskripsi' : journal_research_edit.deskripsi,
        'cover_jurnal' : journal_research_edit.cover_jurnal,
        'link_view_jurnal' : journal_research_edit.link_view_jurnal,
        'link_current_issue' : journal_research_edit.link_current_issue,
        'link_online_submission' : journal_research_edit.link_online_submission,
        'link_download_template' : journal_research_edit.link_download_template,
        'jenis_journal' : journal_research_edit.jenis_journal,
    }
    journal_research_form_edit = JournalUmktForm(request.POST or None,request.FILES or None, initial=data_edit , instance=journal_research_edit)
    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'cover_jurnal' in result_request
        if cek_image == False:
            if journal_research_edit.cover_jurnal:
                if os.path.isfile(journal_research_edit.cover_jurnal.path) == True:
                    os.remove(journal_research_edit.cover_jurnal.path)

    if request.method == "POST" and journal_research_form_edit.is_valid():
        journal_research_form_edit.save()
        messages.info(request, 'Data Journal of Social Research Berhasil di Edit')
        return redirect('journal_research_backend')
    else:
        print(journal_research_form_edit.errors)

    context = {
        'form': journal_research_form_edit,
    }
    return render(request, 'landingpage/backend/journal_research_backend_update.html', context)

def journal_research_backend_detail(request,id):
    data = JournalUmktModel.objects.get(id=id)
    context = {
        'data': data,
    }
    return render(request, 'landingpage/backend/journal_research_backend_detail.html', context)

def downloads_backend(request):
    download_form = DownloadForm(request.POST,request.FILES or None)
    data = DownloadContent.objects.all()
    if request.method == 'POST':
        if download_form.is_valid():
            download_form.save()
            messages.success(request, 'Data Download Berhasil di Tambahkan')
            return redirect('downloads_backend')
        else:
            print(download_form.errors)
    
    context = {
        'form': download_form,
        'Data': data,
    }
    return render(request, 'landingpage/backend/download_backend.html', context)

def downloads_backend_update(request, id):
    download_edit = DownloadContent.objects.get(id=id)

    data_edit = {
        'nama_file' : download_edit.nama_file,
        'jenis_file' : download_edit.jenis_file,
        'ukuran_file' : download_edit.ukuran_file,
        'file_download' :download_edit.file_download,
    }
    download_form_edit = DownloadForm(request.POST or None,request.FILES or None, initial=data_edit , instance=download_edit)
    
    if request.method == 'POST':
        result_request = dict(request.POST)
        #ambil data cek image
        cek_image = 'file_download' in result_request
        if cek_image == False:
            if download_edit.file_download:
                if os.path.isfile(download_edit.file_download.path) == True:
                    os.remove(download_edit.file_download.path)

    if request.method == "POST" and download_form_edit.is_valid():
        download_form_edit.save()
        messages.info(request, 'Data Download Berhasil di Edit')
        return redirect('downloads_backend')
    else:
        print(download_form_edit.errors)

    context = {
        'form': download_form_edit,
    }
    return render(request, 'landingpage/backend/download_backend_update.html', context)

def downloads_backend_delete(request, id):
    data = get_object_or_404(DownloadContent,id=id)
    
    if os.path.isfile(data.file_download.path) == True:
        os.remove(data.file_download.path)
    DownloadContent.objects.filter(id=id).delete()
    messages.error(request, 'Data Download Berhasil di Hapus')
    return redirect('downloads_backend' )