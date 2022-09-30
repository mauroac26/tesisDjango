function table(tabla){
    $('#'+ tabla).DataTable({
      
          // pageLength: 5,
          // "language": {
          //   "url": "//cdn.datatables.net/plug-ins/1.10.15/i18n/Spanish.json"
          // }
          "ordering": false,
          "language": {
           
            "emptyTable": "No hay información",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
            "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
            "infoFiltered": "(Filtrado de _MAX_ total entradas)",
            "lengthMenu": "Mostrar _MENU_ Entradas",
            "loadingRecords": "Cargando...",
            "processing": "Procesando...",
            "search": "Buscar:",
            "zeroRecords": "Sin resultados encontrados",
            "paginate": {
                "first": "Primero",
                "last": "Ultimo",
                "next": "Siguiente",
                "previous": "Anterior"
            }
          },
          responsive: "true",
          dom: 'Bfrtilp',
          buttons:[
            {
              extend: 'excelHtml5',
              text: '<i class="fas fa-file-excel fa-1x"></i>',
              titleAttr: 'Exportar a Excel',
              className: 'btn btn-success btn-sm'
            },
            {
              extend: 'pdfHtml5',
              text: '<i class="fas fa-file-pdf fa-1x"></i>',
              titleAttr: 'Exportar a PDF',
              className: 'btn btn-primary btn-sm'
            },
            {
              extend: 'print',
              text: '<i class="fas fa-print fa-1x"></i>',
              titleAttr: 'Exportar a Imprimir',
              className: 'btn btn-secondary btn-sm'
            
  
            }
          ]
        });
  }


 function cantidadPed(){
  
  $.ajax({
    type: "get",
    dataType: 'json',
     url:  "cantidadPedidos",
  success: function(response) {
    
      var cantidad = response.data;
      
      document.getElementById('divPedidos').innerText = cantidad
        document.getElementById('badgePedidos').className = "badge badge-info badge-pill ml-2 d-inline";
        document.getElementById('badgePedidos').innerText = cantidad
    //   if(cantidad > 0){
    //     document.getElementById('badgePedidos').className = "badge badge-info badge-pill ml-2 d-block";
    //     document.getElementById('badgePedidos').innerText = cantidad
    //     // document.getElementById('badgePedidosStock').className = "badge badge-info badge-pill ml-2 d-inline";
    //     // document.getElementById('badgePedidosStock').innerText = cantidad
        
    //   }
    //   else{
    //     document.getElementById('badgePedidos').className = "badge badge-info badge-pill ml-2 d-none";
    //     // document.getElementById('badgePedidosStock').className = "badge badge-info badge-pill ml-2 d-none";
    //   }
  
  }
  });
  

}