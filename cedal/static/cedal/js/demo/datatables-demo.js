// Call the dataTables jQuery plugin
// $(document).ready(function() {
//   $('#dataTable').DataTable({
//     // "language": {
//     //   "url": "//cdn.datatables.net/plug-ins/1.10.15/i18n/Spanish.json"
//     // }
//     "language": {
//       "decimal": "",
//       "emptyTable": "No hay información",
//       "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
//       "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
//       "infoFiltered": "(Filtrado de _MAX_ total entradas)",
//       "infoPostFix": "",
//       "thousands": ",",
//       "lengthMenu": "Mostrar _MENU_ Entradas",
//       "loadingRecords": "Cargando...",
//       "processing": "Procesando...",
//       "search": "Buscar:",
//       "zeroRecords": "Sin resultados encontrados",
//       "paginate": {
//           "first": "Primero",
//           "last": "Ultimo",
//           "next": "Siguiente",
//           "previous": "Anterior"
//       }
//     }
//   });
// });

function table(tabla){
  $('#'+ tabla).DataTable({
        // pageLength: 5,
        // "language": {
        //   "url": "//cdn.datatables.net/plug-ins/1.10.15/i18n/Spanish.json"
        // }
        
        "language": {
          "decimal": "",
          "emptyTable": "No hay información",
          "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
          "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
          "infoFiltered": "(Filtrado de _MAX_ total entradas)",
          "infoPostFix": "",
          "thousands": ",",
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