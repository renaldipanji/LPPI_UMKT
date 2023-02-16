from .models import *
import uuid
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from .functions import group_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout, update_session_auth_hash
from django.contrib.auth.models import Group
from .forms import RegisterForm, LoginForm,ProfilForm,ProfilFotoForm
from django.contrib import messages
from .helpers import *

# Create your views here.
def login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        # pass
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username,password=password)
            if user is not None:
                try:
                    user_group = Group.objects.get(user = user)
                except Group.DoesNotExist:
                    user_group  = None
                auth_login(request, user)
                if user_group is not None:
                    pass
                else:
                    my_group = Group.objects.get(name='pengguna')   
                    my_group.user_set.add(user)     
                return redirect('dashboard')
            else:
                user_id = User.objects.filter(username=username).first()
                msg = 'Username atau Password tidak valid'
                if user_id:
                    if not user_id.is_active:
                        msg = "User Belum Aktif Silahkan Verifikasi Email Dulu"
                else:
                    msg = 'Username atau Password tidak valid'
        else:
            msg = 'validasi form error'
        print(form.errors)
    return render(request, 'akun/login.html', {'form':form, 'msg' : msg})

def daftar(request):
    msg = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user , forgot_password_token = token)
            profile_obj.save()
            domain = request.get_host()
            ssl = request.is_secure()
            send_verif_mail(user.email, token, domain, ssl)            
            msg = 'Akun Berhasil di Buat'
            return redirect('daftar_berhasil')
        else:
            msg = 'Form is Valid'
            print(form.errors)
    else:
        form = RegisterForm()            
    return render(request, 'akun/daftar.html', {'form': form, 'msg':msg})

def lupaPassword(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            if not User.objects.filter(email = email).first():
                messages.error(request, 'Email tidak ditemukan.')
                return redirect('lupaPassword')

            user_obj = User.objects.get(email = email)
            token = str(uuid.uuid4())
            profile_obj = Profile.objects.get(user_id = user_obj.id)
            profile_obj.forgot_password_token = token
            profile_obj.save()
            domain = request.get_host()
            ssl = request.is_secure()
            send_forget_password_mail(user_obj.email, token, domain, ssl)
            return redirect('konfirmasi_reset_pass')
    except Exception as e:
        print (e)    
    return render(request, 'akun/lupa_password.html')

def changePassword(request, token):
    context = {}
    try:
        profile_obj = Profile.objects.get(forgot_password_token = token)
        context = {'user_id' : profile_obj.user.id}
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')
            print(user_id)
            if user_id is  None:
                messages.success(request, 'User tidak ditemukan.')
                return redirect(f'/change-password/{token}/')        
            
            if  new_password != confirm_password:
                messages.success(request, 'Password tidak sama.')
                return redirect(f'/change-password/{token}/')
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            messages.success(request, 'Password berhasil diganti.')
            return redirect('login')
    except Exception as e:
        print(e)
    return render(request, 'akun/change_password.html', context)

# def resetPassword(request):
#     return render(request, 'akun/reset_password.html')

def konfVerifAkun(request):
    return render(request, 'akun/konf_email_verifikasi_akun.html')

def verifAkun(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')

            if not User.objects.filter(email = email).first():
                messages.error(request, 'Email tidak ditemukan.')
                return redirect('verifikasi_akun')
            user_obj = User.objects.get(email = email)
            token = str(uuid.uuid4())
            profile_obj = Profile.objects.get(user_id = user_obj.id)
            profile_obj.forgot_password_token = token
            profile_obj.save()
            domain = request.get_host()
            ssl = request.is_secure()
            send_verif_mail(user_obj.email, token, domain, ssl)
            return redirect('konfirm_verif_akun')
    
    except Exception as e:
        print (e)      
    return render(request, 'akun/verifikasi_email.html')

def verifBerhasil(request, token):
    profile_obj = Profile.objects.get(forgot_password_token = token)
    user_obj = User.objects.get(id = profile_obj.user_id)
    if user_obj.is_active == False :
        user_obj.is_active = True
        user_obj.save()
        messages.success(request, 'Akun telah diverifikasi, silahkan login.')
        return redirect('login')
    return render(request, 'akun/daftar_berhasil.html')

def logout_view(request):
    logout(request)
    return render(request, 'akun/logout_berhasil.html')

@login_required(login_url='login')
def profil(request):
    dataUser = get_object_or_404(User,id=request.user.id)
    form = ProfilForm(request.POST or None, instance = dataUser)
    formFoto = ProfilFotoForm(request.POST, request.FILES or None, instance = dataUser)
    if request.method == "POST":
        if request.POST["keperluan"] == "gantipass":
            user = User.objects.get(id=request.user.id)
            current_password = request.user.password
            old_password = request.POST.get('old_password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')

            matchcheck = check_password(old_password, current_password)
            form = ProfilForm(instance = dataUser)
            if matchcheck:
                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()
                    update_session_auth_hash(request, user)
                    messages.success(request, 'Password berhasil diganti.')
                    redirect("profil")
                else:
                    messages.error(request, 'Konfirmasi password tidak sama!')
                    redirect("profil")
            else:
                messages.error(request, 'Password Lama anda salah !!!')
                redirect("profil")
        elif request.POST["keperluan"] == "editfoto":
            result_request = dict(request.POST)
            print(result_request)
            # ambil data cek image
            cek_image = 'foto_profile' in result_request
            if cek_image == False:
                if request.user.foto_profile :
                    if os.path.isfile(dataUser.foto_profile.path) == True:
                        os.remove(dataUser.foto_profile.path)
            if formFoto.is_valid():
                formFoto.save()
                form = ProfilForm(instance = dataUser)
                formFoto = ProfilFotoForm(instance = dataUser)
                messages.success(request, 'Foto Profil Berhasil diedit.')
                return redirect('profil')
        if form.is_valid():
            if request.POST["keperluan"] == "editprofil":
                form.save()
        else:
            print(form.errors)
    user = User.objects.get(username=request.user)
    data = {
            'id': user.id,
            'email': user.email,
            'nama' : user.nama,
            'no_hp' : user.no_hp,
            'institusi' : user.nama_institusi,
            'form': form,
            'formFoto': formFoto
    }
    return render(request, 'akun/profil.html', data)