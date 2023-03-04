/*----------------------------- DEKLARASI VARIABEL -----------------------------*/

/*************** Element Target ***************/ 
const data_matkul         = document.getElementById('data_matkul')
const data_validasi_opl   =  document.getElementById('data_validasi_opl')
const data_team_tech   =  document.getElementById('data_team_tech')
/*************** Element Target ***************/ 

/*************** Content Form ***************/ 
let form_matkul_tambah;
/*************** Content Form ***************/ 
/*----------------------------- DEKLARASI VARIABEL -----------------------------*/


/*----------------------------- BACKEND AJAX CRUD -----------------------------*/ 

/*************** Menampilkan List Data Mata Kuliah ***************/ 
showDataValidasiOpl()
showDataMatkul()
/*************** Menampilkan List Data Mata Kuliah ***************/ 


/*************** Logic Menampilkan List Data ***************/
  /*==========* Event Menampilkan List Data Mata Kuliah *==========*/
  function showDataMatkul(){
    $.ajax({
      type: 'GET',
      url: '/validasi-openlearning/show-data-matkul/',
      success: function(response){
        data = response.data
        let number = 1
        data_matkul.innerHTML = ''
        
        data.forEach(el => {
          data_matkul.innerHTML += `
          <tr>
            <td>${number}</td>
            <td>${el.kode_matkul}</td>
            <td>${el.nama_matkul}</td>
            <td><a href="${el.link_matkul}">Buka</a></td>
            <td>${el.pemilik_course}</td>
            <td>
              <a class="btn btn-primary btn-sm mr-1" href="/validasi-openlearning-detail/${el.id}/">
                <span class="fas fa-user-plus"></span> Team Teaching 
              </a>
              <button type="button" class="btn btn-info btn-sm mr-1 btn-modal-edit" data-bs-toggle="modal" data-id="${el.id}" data-bs-target="#modal_edit">
                <span class="fas fa-edit"></span> Edit 
              </button>
              <button type="button" class="btn btn-danger btn-sm btn-modal-hapus" data-bs-toggle="modal" data-id="${el.id}" data-bs-target="#modal_hapus">
              <span class="fas fa-trash"></span> Hapus
              </button>
            </td>
          </tr>
          `
          number++;
        });
      },
      error: function(error){
        console.log(error)
      }
    })
  }
  /*==========* Fungsi Menampilkan List Data Mata Kuliah *==========*/
  /*==========* Fungsi Menampilkan List Data Validasi OPL *==========*/
  function showDataValidasiOpl(){
    $.ajax({
      type: 'GET',
      url: '/validasi-openlearning/show-data-matkul/',
      success: function(response){
        data = response.data
        let number = 1
        data_validasi_opl.innerHTML = ''
        
        data.forEach(el => {
          data_validasi_opl.innerHTML += `
          <tr>
            <td>${number}</td>
            <td>${el.kode_matkul}</td>
            <td>${el.nama_matkul}</td>
            <td>${el.progres}%</td>
            <td><span class="badge bg-${el.badge}">${el.status_haki}</span></td>
            <td>${el.keterangan}</td>
            <td>
            <button type="button" class="btn btn-primary btn-sm btn_modal_validasi_opl" data-id="${el.id}" data-bs-toggle="modal" data-bs-target="#modal_validasi_opl">
              Validasi
            </button>
            </td>
          </tr>
          `
          number++;
        });
      },
      error: function(error){
        console.log(error)
      }
    })
  }
  /*==========* Fungsi Menampilkan List Data Validasi OPL *==========*/
  
  /*==========* Fungsi Menampilkan List Data Validasi OPL *==========*/
  function showDataTeamTeaching(dataId){
    $.ajax({
      type: 'GET',
      url: '/validasi-openlearning/show-data-team-teaching/'+dataId+'/',
      success: function(response){
        data = response.data
        let number = 1
        data_team_tech.innerHTML = ''
        
        data.forEach(el => {
          data_team_tech.innerHTML += `
          <tr>
            <td>${number}</td>
            <td>${el.team_teaching}</td>
            <td>${el.prodi}</td>
            <td>
            <button type="button" class="btn btn-danger btn-sm btn_delete_team_teach" data-id="${el.id}">
              Hapus
            </button>
            </td>
          </tr>
          `
          number++;
        });
        $(document).ready(function() {
          /** reset form tambah matkul **/
          $('.btn_delete_team_teach').click(function(){
            var dataId = $(this).data('id');
            $.ajax({
              type:"POST",
              url: '/validasi-openlearning/hapus-team-teach/' + dataId + '/',
              data: {
                'csrfmiddlewaretoken': $('[name=csrfmiddlewaretoken]').val(),
                'id': dataId
              },
              success: function(response){
                var data_matkul = response.data_hapus
                SweetAlert('success', `Data "${data_matkul}" Berhasil di Di Hapus`)
                $('#modal_teamteaching').modal('hide')
                showDataMatkul()
                showDataValidasiOpl()
              },
              error: function(error){
                SweetAlert('error', 'Ups... ada yang salah, harap cek kembali!')
              }
            })
          });
        });
      },
      error: function(error){
        console.log(error)
      }
    })
  }
  /*==========* Fungsi Menampilkan List Data Validasi OPL *==========*/
/*************** Logic Menampilkan List Data ***************/ 


/*************** Logic Menambahkan Data Mata Kuliah ***************/ 
  /** reset form tambah matkul **/
  $('#btn_tambah_matkul').click(function(){
    $('#form_matkul').trigger('reset')
    if($('#form_matkul').find('#content_form_matkul_tambah').length <= 0){
      form_matkul_tambah.prependTo('#form_matkul')
    }
  });
  /** reset form tambah matkul **/
  /*^^^^^^^^^^* Event Menambahkan Data Mata Kuliah *^^^^^^^^^^*/ 
  $('#form_matkul').submit(e =>{
    e.preventDefault()
    var data_matkul = new FormData()
    data_matkul.append('csrfmiddlewaretoken',$('[name=csrfmiddlewaretoken]').val())
    data_matkul.append('kode_matkul', $('#id_kode_matkul').val())
    data_matkul.append('nama_matkul', $('#id_nama_matkul').val())
    data_matkul.append('link_matkul', $('#id_link_matkul').val())
    data_matkul.append('prodi', $('select[name=prodi]').val())
    data_matkul.append('pemilik_course', $('select[name=pemilik_course]').val())

    $.ajax({
      type: "POST",
      url: '',
      MimeType: 'multipart/form-data',
      contentType:false,
      processData:false,
      data: data_matkul,
      success: function(response){
        showDataMatkul()
        showDataValidasiOpl()
        SweetAlert('success', 'Data mata kuliah berhasil ditambahkan')
        $('#form_matkul')[0].reset()
        $('#modal_tambah').modal('hide')
      },
      error: function(error){
        SweetAlert('error','Ups... ada yang salah' ,'Cek kembali data yang anda masukkan!')
      }
    })
  })
  /*^^^^^^^^^^* Event Menambahkan Data Mata Kuliah *^^^^^^^^^^*/ 
/*************** Logic Menambahkan Data Mata Kuliah ***************/ 


  /*^^^^^^^^^^* Event Filter Data Validasi OPL *^^^^^^^^^^*/ 
  $(document).ready(function() {
  $('#btn_filter_validasi_opl').click(function(){
    var data_filter = $('#validasi_opl_filter').val()
    let target_url = '/validasi-openlearning/filter-data-validasi-opl/'+ data_filter +'/'
    $.ajax({
      type: 'GET',
      url: target_url,
      success: function(response){
        data = response.data
          let number = 1
          data_validasi_opl.innerHTML = ''
          /** cek data validasi OPL **/ 
          if (data.length == 0 ){
            data_validasi_opl.innerHTML = '<tr class="odd"><td valign="top" colspan="7" class="dataTables_empty text-danger">Data Program Studi ini tidak ditemukan</td></tr>'
          }
          else{
            data.forEach(el => {
              data_validasi_opl.innerHTML += `
              <tr>
                <td>${number}</td>
                <td>${el.kode_matkul}</td>
                <td>${el.nama_matkul}</td>
                <td>${el.progres}%</td>
                <td><span class="badge bg-${el.badge}">${el.status_haki}</span></td>
                <td>${el.keterangan}</td>
                <td>
                <button type="button" class="btn btn-primary btn-sm btn_modal_validasi_opl" data-id="${el.id}" data-bs-toggle="modal" data-bs-target="#modal_validasi_opl">
                  Validasi
                </button>
                </td>
              </tr>
              `
              number++;
          });
          }
          /** cek data validasi OPL **/ 
      },
      error: function(error){
        console.log(error)
      }
    })
  })
  });
  /*^^^^^^^^^^* Event Filter Data Validasi OPL *^^^^^^^^^^*/ 
  /*^^^^^^^^^^* Event Filter Data Mata Kuliah *^^^^^^^^^^*/ 
  $(document).ready(function() {
  $('#btn_filter_data_matkul').click(function(){
    var data_filter = $('#filter_data_matkul').val()
    let target_url = '/validasi-openlearning/filter-data-matkul/'+ data_filter +'/'
    $.ajax({
      type: 'GET',
      url: target_url,
      success: function(response){
        data = response.data
        let number = 1
        data_matkul.innerHTML = ''
        if (data.length == 0 ){
          data_matkul.innerHTML = '<tr class="odd"><td valign="top" colspan="7" class="dataTables_empty text-danger">Data Program Studi ini tidak ditemukan</td></tr>'
        }
        data.forEach(el => {
          data_matkul.innerHTML += `
          <tr>
            <td>${number}</td>
            <td>${el.kode_matkul}</td>
            <td>${el.nama_matkul}</td>
            <td><a href="${el.link_matkul}">Buka</a></td>
            <td>${el.pemilik_course}</td>
            <td>
              <button type="button" class="btn btn-info btn-sm mr-1 btn-modal-edit" data-bs-toggle="modal" data-id="${el.id}" data-bs-target="#modal_edit">
                <span class="fas fa-edit"></span> Edit 
              </button>
              <button type="button" class="btn btn-danger btn-sm btn-modal-hapus" data-bs-toggle="modal" data-id="${el.id}" data-bs-target="#modal_hapus">
              <span class="fas fa-trash"></span> Hapus
              </button>
            </td>
          </tr>
          `
          number++;
        });
      },
      error: function(error){
        console.log(error)
      }
    })
  })
});
  /*^^^^^^^^^^* Event Filter Data Mata Kuliah *^^^^^^^^^^*/ 
/*************** Logic Filter Data ***************/ 

/*************** Logic Menampilkan Detail Data ***************/
  /*^^^^^^^^^^* Event Menampilkan Detail Data Mata Kuliah Edit*^^^^^^^^^^*/ 
    $('#table_biasa').on('click', '.btn-modal-edit', function() {
      form_matkul_tambah = $('#content_form_matkul_tambah').detach() // menghapus sementara content form matkul tambah
      var dataId = $(this).data('id');
      $.ajax({
        type: 'GET',
        url: '/validasi-openlearning/detail-matkul/' + dataId + '/',
        success: function(response){
          data = response.dataDetailMatkul
          $('[name="kode_matkul"]').val(data.kode_matkul)
          $('[name="nama_matkul"]').val(data.nama_matkul)
          $('[name="link_matkul"]').val(data.link_matkul)
          $('[name="pemilik_course"]').val(data.pemilik_course)
          $('[name="prodi"]').val(data.prodi)
          $('#submit_edit_matkul').attr('data-id', dataId)
          $('#submit_tambah_team_teach').attr('data-id', dataId)
        },
        error: function(error){
          console.log(error)
        }
      })
    });
  /*^^^^^^^^^^* Event Menampilkan Detail Data Mata Kuliah Edit*^^^^^^^^^^*/ 
   
  /*^^^^^^^^^^* Event Menampilkan Detail Data Mata Kuliah Hapus*^^^^^^^^^^*/
  $('#table_biasa').on('click', '.btn-modal-hapus', function() {
    var dataId = $(this).data('id');
    $.ajax({
      type: 'GET',
      url: '/validasi-openlearning/detail-matkul/' + dataId + '/',
      success: function(response){
        data = response.dataDetailMatkul
        $('#btn_hapus_matkul').attr('data-id', data.id)
        $('#kode_matkul_hapus').text(data.kode_matkul)
        $('#nama_matkul_hapus').text(data.nama_matkul)
        $('#link_matkul_hapus').text(data.link_matkul)
        $('#pemilik_course_hapus').text(data.pemilik_course_nama)
      },
      error: function(error){
        console.log(error)
      }
    })
  })
  /*^^^^^^^^^^* Event Menampilkan Detail Data Mata Kuliah Hapus*^^^^^^^^^^*/

  /*^^^^^^^^^^* Event Menampilkan Detail Data Validasi OPL*^^^^^^^^^^*/
  $('#table_default').on('click', '.btn_modal_validasi_opl', function() {
    var dataId = $(this).data('id');
    $.ajax({
      type: 'GET',
      url: '/validasi-openlearning/detail-matkul/' + dataId + '/',
      success: function(response){
        data = response.dataDetailMatkul
        $('#modal_validasi_opl_label').text(data.nama_matkul)
        $('[name="ch1"]').val(data.ch1)
        $('[name="ch2"]').val(data.ch2)
        $('[name="ch3"]').val(data.ch3)
        $('[name="ch4"]').val(data.ch4)
        $('[name="ch5"]').val(data.ch5)
        $('[name="ch6"]').val(data.ch6)
        $('[name="ch7"]').val(data.ch7)
        $('[name="ch8"]').val(data.ch8)
        $('[name="ch9"]').val(data.ch9)
        $('[name="ch10"]').val(data.ch10)
        $('[name="ch11"]').val(data.ch11)
        $('[name="ch12"]').val(data.ch12)
        $('[name="ch13"]').val(data.ch13)
        $('[name="ch14"]').val(data.ch14)
        $('[name="status_haki"]').val(data.status_haki)
        $('[name="keterangan"]').text(data.keterangan)
        $('#submit_validasi_opl').attr('data-id', dataId)
      },
      error: function(error){
        console.log(error)
      }
    })
  })
  /*^^^^^^^^^^* Event Menampilkan Detail Data Validasi OPL*^^^^^^^^^^*/
  
/*************** Logic Menampilkan Detail Data ***************/ 

/*************** Logic Mengedit Data Mata Kuliah ***************/
  /*^^^^^^^^^^* Event Mengedit Data Mata Kuliah*^^^^^^^^^^*/
  $('#form_matkul_edit').submit(e=>{
    e.preventDefault()
    var dataId = $('#submit_edit_matkul').attr('data-id')
    var data_matkul_update = new FormData()
    data_matkul_update.append('csrfmiddlewaretoken',$('[name=csrfmiddlewaretoken]').val())
    data_matkul_update.append('kode_matkul', $('#id_kode_matkul').val())
    data_matkul_update.append('nama_matkul', $('#id_nama_matkul').val())
    data_matkul_update.append('link_matkul', $('#id_link_matkul').val())
    data_matkul_update.append('pemilik_course', $('#id_pemilik_course').val())
    data_matkul_update.append('prodi', $('#id_prodi').val())
  
    $.ajax({
      type:"POST",
      url: '/validasi-openlearning/edit-matkul/' + dataId + '/',
      MimeType: 'multipart/form-data',
      contentType:false,
      processData:false,
      data: data_matkul_update,
      success: function(response){
        SweetAlert('success', 'Data Berhasil di Edit')
        showDataMatkul()
        showDataValidasiOpl()
        $('#modal_edit').modal('hide')
      },
      error: function(){
        SweetAlert('error','Ups... ada yang salah' ,'Cek kembali data yang anda masukkan!')
      }
    })
  
  })
  /*^^^^^^^^^^* Event Mengedit Data Mata Kuliah*^^^^^^^^^^*/
  /*************** Logic Mengedit Data Mata Kuliah ***************/ 

  
/*************** Logic Validasi Data Mata Kuliah ***************/ 
  /*^^^^^^^^^^* Event Validasi Data Mata Kuliah*^^^^^^^^^^*/
  $('#form_validasi_opl').submit(e=>{
    e.preventDefault()
    var dataId = $('#submit_validasi_opl').attr('data-id')
    var data_validasi_opl = new FormData()
    data_validasi_opl.append('csrfmiddlewaretoken',$('[name=csrfmiddlewaretoken]').val())
    data_validasi_opl.append('ch1', $('#id_ch1').val())
    data_validasi_opl.append('ch2', $('#id_ch2').val())
    data_validasi_opl.append('ch3', $('#id_ch3').val())
    data_validasi_opl.append('ch4', $('#id_ch4').val())
    data_validasi_opl.append('ch5', $('#id_ch5').val())
    data_validasi_opl.append('ch6', $('#id_ch6').val())
    data_validasi_opl.append('ch7', $('#id_ch7').val())
    data_validasi_opl.append('ch8', $('#id_ch8').val())
    data_validasi_opl.append('ch9', $('#id_ch9').val())
    data_validasi_opl.append('ch10', $('#id_ch10').val())
    data_validasi_opl.append('ch11', $('#id_ch11').val())
    data_validasi_opl.append('ch12', $('#id_ch12').val())
    data_validasi_opl.append('ch13', $('#id_ch13').val())
    data_validasi_opl.append('ch14', $('#id_ch14').val())
    data_validasi_opl.append('keterangan', $('#id_keterangan').val())
    data_validasi_opl.append('status_haki', $('#id_status_haki').val())
    const progres = parseInt((parseFloat($('#id_ch1').val()) + parseFloat($('#id_ch2').val()) + parseFloat($('#id_ch3').val()) + parseFloat($('#id_ch4').val()) + parseFloat($('#id_ch5').val()) + parseFloat($('#id_ch6').val()) + parseFloat($('#id_ch7').val()) + parseFloat($('#id_ch8').val()) + parseFloat($('#id_ch9').val()) + parseFloat($('#id_ch10').val()) + parseFloat($('#id_ch11').val()) + parseFloat($('#id_ch12').val()) + parseFloat($('#id_ch13').val()) + parseFloat($('#id_ch14').val())) / 14 * 100)
    data_validasi_opl.append('progres', progres)
    
    $.ajax({
      type:"POST",
      url: '/validasi-openlearning/validasi-opl/' + dataId + '/',
      MimeType: 'multipart/form-data',
      contentType:false,
      processData:false,
      data: data_validasi_opl,
      success: function(response){
        SweetAlert('success', `Course "${response.data_validasi}" ini berhasil di validasi`)
        showDataMatkul()
        showDataValidasiOpl()
        $('#modal_validasi_opl').modal('hide')
      },
      error: function(){
        SweetAlert('error','Ups... ada yang salah' ,'Cek kembali data yang anda masukkan!')
      }
    })
  
  })
  /*^^^^^^^^^^* Event Validasi Data Mata Kuliah*^^^^^^^^^^*/
/*************** Logic Validasi Data Mata Kuliah ***************/ 

/*************** Logic Menghapus Data Mata Kuliah ***************/ 
  /*^^^^^^^^^^* Event Validasi Data Mata Kuliah*^^^^^^^^^^*/
  $('#btn_hapus_matkul').click(function(){
    var dataId = $('#btn_hapus_matkul').attr('data-id')

    $.ajax({
      type:"POST",
      url: '/validasi-openlearning/hapus-matkul/' + dataId + '/',
      data: {
        'csrfmiddlewaretoken': $('[name=csrfmiddlewaretoken]').val(),
        'id': dataId
      },
      success: function(response){
        var data_matkul = response.data_hapus
        SweetAlert('success', `Data "${data_matkul}" Berhasil di Di Hapus`)
        $('#modal_hapus').modal('hide')
        showDataMatkul()
        showDataValidasiOpl()
      },
      error: function(error){
        SweetAlert('error', 'Ups... ada yang salah, harap cek kembali!')
      }
    })

  })
  /*^^^^^^^^^^* Event Validasi Data Mata Kuliah*^^^^^^^^^^*/
/*************** Logic Menghapus Data Mata Kuliah ***************/ 

/*----------------------------- BACKEND AJAX CRUD -----------------------------*/   