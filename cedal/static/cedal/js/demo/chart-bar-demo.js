// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Verdana';
Chart.defaults.global.defaultFontColor = '#858796';

function number_format(number, decimals, dec_point, thousands_sep) {
  // *     example: number_format(1234.56, 2, ',', ' ');
  // *     return: '1 234,56'
  number = (number + '').replace(',', '').replace(' ', '');
  var n = !isFinite(+number) ? 0 : +number,
    prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
    sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
    dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
    s = '',
    toFixedFix = function(n, prec) {
      var k = Math.pow(10, prec);
      return '' + Math.round(n * k) / k;
    };
  // Fix for IE parseFloat(0.55).toFixed(0) = 0;
  s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
  if (s[0].length > 3) {
    s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
  }
  if ((s[1] || '').length < prec) {
    s[1] = s[1] || '';
    s[1] += new Array(prec - s[1].length + 1).join('0');
  }
  return s.join(dec);
}




$.ajax({
  type: "get",
  dataType: 'json',
   url:  "graficoClientes",
success: function(response) {
  var paramClientes = [];
  var paramCantidad = [];
    var pe = response.clientes;
    //alert(pe);
                 $.each(pe, function(i, item){
                  //const shortMonthName = moment(item.id_compra__fecha).format('MMM');
                  paramClientes.push(item.cuit__nombre);
              
                  paramCantidad.push(item.cantidad); 
                                        
            
                
                 });
// Bar Chart Example
var ctx = document.getElementById("myBarChart");
var myBarChart = new Chart(ctx, {
  type: 'horizontalBar',
  data: {
    labels: paramClientes,
    datasets: [{
      axis: 'x',
      label: "Cantidad",
      data: paramCantidad,
      fill: false,
      backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(255, 159, 64, 0.2)',
        'rgba(255, 205, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        // 'rgba(153, 102, 255, 0.2)',
        // 'rgba(201, 203, 207, 0.2)'
      ],
      borderColor: [
        'rgb(255, 99, 132)',
        'rgb(255, 159, 64)',
        'rgb(255, 205, 86)',
        'rgb(75, 192, 192)',
        'rgb(54, 162, 235)',
        // 'rgb(153, 102, 255)',
        // 'rgb(201, 203, 207)'
      ],
      borderWidth: 1
    }],
  },
  options: {
    
      tooltips: {
        enabled: true
      },
      responsive: true,
      legend: {
         display: false,
      },
      scales: {
         yAxes: [{
           barPercentage: 0.50,
           gridLines: {
             display: true,
             drawTicks: true,
             drawOnChartArea: false
           },
           ticks: {
             fontColor: '#555759',
             fontFamily: 'Verdana',
             fontSize: 11
           }
            
         }],
         xAxes: [{
             gridLines: {
               display: true,
               drawTicks: false,
               tickMarkLength: 10,
               drawBorder: false
             },
           ticks: {
             padding: 5,
             beginAtZero: true,
             fontColor: '#555759',
             fontFamily: 'Verdana',
             fontSize: 11,
             callback: function(label, index, labels) {
              return label/1;
             }
               
            },
            // scaleLabel: {
            //   display: true,
            //   padding: 10,
            //   fontFamily: 'Verdana',
            //   fontColor: '#555759',
            //   fontSize: 16,
            //   fontStyle: 700
            // },
           
         }]
      }
    
  }
});

}
});