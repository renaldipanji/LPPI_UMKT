/*----------------------------- Fungsi Alert -----------------------------*/ 

/*************** Bootstrap Alert ***************/
const handleAlerts = (pesan_box,type, msg)=>{
    pesan_box.innerHTML=`
    <div class="alert alert-${type} alert-dismissible fade show" role="alert">
        ${msg}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
    `
}
/*************** Bootstrap Alert ***************/

/*************** SweetAlert2 Alert ***************/
const SweetAlert = (type, judul, msg)=>{
    if (typeof msg == "undefined"){
        Swal.fire({
            icon: `${type}`,
            title: `${judul}`,
            showConfirmButton: false,
            timer: 1800
          })
    }
    else if (typeof msg != "undefined"){
        Swal.fire({
            icon: `${type}`,
            title: `${judul}`,
            text: `${msg}`
          })
    }
}
/*************** SweetAlert2 Alert ***************/

/*************** Validasi Ukuran Foto ***************/
const imageValidation = (idfile)=>{
    if (window.File && window.FileReader && window.FileList && window.Blob) {
        var file = $(idfile)[0].files[0];
        if (file && file.size > 1 * 1024 * 1024) {
            var pesan = "Ukuran File " + file.name + " Melebihi 1 MB"
            SweetAlert('error','Harap Input Ulang', pesan)
            return false;
        }
        return true;
      }
}
/*************** Validasi Ukuran Foto ***************/
/*************** Validasi Ukuran Foto ***************/
const fileValidation = (idfile)=>{
    if (window.File && window.FileReader && window.FileList && window.Blob) {
        var file = $(idfile)[0].files[0];
        var pathFile = $(idfile).val()
        var ekstensiOk = /(\.pdf|\.doc|\.docx|\.jpeg)$/i;
        if(!ekstensiOk.exec(pathFile)){
            var pesan = "Ektensi File tidak diterima"
            SweetAlert('error','Harap Input Ulang', pesan)
            return false;
        }
        if (file && file.size > 1 * 1024 * 1024) {
            var pesan = "Ukuran File " + file.name + " Melebihi 1 MB"
            SweetAlert('error','Harap Input Ulang', pesan)
            return false;
        }
        return true;
      }
}
/*************** Validasi Ukuran Foto ***************/
/*----------------------------- Fungsi Alert -----------------------------*/ 

/*----------------------------- Validasi Input -----------------------------*/ 
function onlyNumber(evt) {
    var charCode = (evt.which) ? evt.which : event.keyCode
     if (charCode > 31 && (charCode < 48 || charCode > 57))

      return false;
    return true;
  }
const onlyNumberInput = (id_input) =>{

    $(id_input).attr('onkeypress', 'return onlyNumber(event)');
    $('#form_edit').attr('onkeypress','return event.keyCode != 13')
}  
/*----------------------------- Validasi Input -----------------------------*/ 

/*----------------------- CUSTOM ELEMENT HTML -----------------------*/ 
/*************** Custom File Input ***************/
function addLabelImage(fileInput,id_input,targetLabel){
    $(fileInput).change(function(e){
        var fileName = e.target.files[0].name;
        $(id_input).find(targetLabel).html(fileName);
    });
}
/*************** Custom File Input ***************/

/*----------------------------- Fungsi Check Box -----------------------------*/
function checkBoxStudio(){
    $('.form-check-input').click(function(){
        var txt="";
        $('.form-check-input:checked').each(function(){
            txt+=$(this).val()+", "
        });
        $('#id_jenis_booking').val(txt);
    })
}
/*----------------------------- Fungsi Check Box -----------------------------*/
/*----------------------- CUSTOM ELEMENT HTML -----------------------*/

/*----------------------- CONDITION ELEMENT HTML -----------------------*/ 
/*************** Hide Button Hapus dan Lihat ***************/
function hideBtnUsr(data_id, status){
    if (status == "1" || status == "2" || status == "3"){
        var selector_id = `[data_id="${data_id}"]`
        $(selector_id).find('.btn-modal-hapus').hide()
        $(selector_id).find('.btn-modal-batal').hide()
        $(selector_id).find('.modal-footer').hide() 
        
        /** Catatan Pesan */
        document.getElementById("status_lihat").insertAdjacentHTML('beforeend','<div class="fs-6"><strong>Catatan: </strong> Data tidak dapat diubah apabila status telah diproses. Jika ingin merubah status, silahkan menghubungi<a class="text-decoration-none" href="http://127.0.0.1:8000/#tentangkami" target="_blank" rel="noopener noreferrer"> Admin</a></div>');
    }
    else {
        $('.modal-footer').show()
    }
}
/*************** Hide Button Hapus dan Lihat ***************/

/*************** Aksi Saat Tambah Data Sukses   ***************/
const createSuccess = () =>{
    SweetAlert('success','Data berhasil ditambahkan')
    /* Reset Label KTP dan Surat */
    $('#input_upload_ktp').find('.custom-file-label').html('Pilih File')
    $('#input_upload_surat').find('.custom-file-label').html('Pilih File')
    $('#input_upload_image').find('.custom-file-label').html('Pilih File')
    /* Reset Label KTP dan Surat */    
    $('#form_tambah').trigger('reset')
    $('#custom-tabs-one-profile-tab').removeClass("active")
    $('#custom-tabs-one-home-tab').addClass("active")
    $('#custom-tabs-one-profile').removeClass("show active")
    $('#custom-tabs-one-home').addClass("show active")
}
/*************** Aksi Saat Tambah Data Sukses   ***************/
/*************** Aksi Saat Update Data Sukses   ***************/
const updateSuccess = () =>{
    SweetAlert('success','Data berhasil diedit')
    /* Reset Label KTP dan Surat */
    $('#update_upload_ktp').find('.custom-file-label').html('Pilih File')
    $('#update_upload_surat').find('.custom-file-label').html('Pilih File')
    $('#update_upload_image').find('.custom-file-label').html('Pilih File')
    /* Reset Label KTP dan Surat */
    $('#modal-lihat').modal('hide')
    $('#form_edit').trigger('reset')
}
/*************** Aksi Saat Update Data Sukses   ***************/

/*----------------------- CONDITION ELEMENT HTML -----------------------*/ 