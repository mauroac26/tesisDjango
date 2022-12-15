// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Verdana', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
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


function comparativa(year1, year2){
    
var paramPrecio2021 = ['0','0','0','0','0','0','0','0','0','0','0','0'];
var paramPrecio2022 = ['0','0','0','0','0','0','0','0','0','0','0','0'];


fecha = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"];


$.ajax({
  type: "get",
  dataType: 'json',
   url:  "/graficoVentasYear",
   data: {year1,
        year2},
success: function(response) {
  
    var pe = response.venta1;
   
    var com = response.venta2;
  
                
                 $.each(pe, function(i, item){
                  
                                        
                  paramPrecio2021[item.id_venta__fecha__month - 1] = parseFloat(item.total__sum).toFixed(2)
                
                 });

                 $.each(com, function(i, item){
                 

                  paramPrecio2022[item.id_venta__fecha__month - 1] = parseFloat(item.total__sum).toFixed(2)
                                        
            
                
                 });





var ctx = document.getElementById("myAreaChartVentas");

var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: fecha,
    datasets: [{ 
        data: paramPrecio2021,
        label: "Ventas" + " " + year1,
        borderColor: "#F90505",
        fill: false
      }, { 
        data: paramPrecio2022,
        label: "Ventas" + " " + year2,
        borderColor: "#069A3E",
        fill: false
      }
    ]
  },
  options: {
    maintainAspectRatio: false,
 
    tooltips: {
      
      callbacks: {
        label: function(tooltipItem, chart) {
          var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
          return datasetLabel + ': $' + number_format(tooltipItem.yLabel);
        }
      }
    },
  
    scales: {
      
      yAxes: [{
        ticks: {
          maxTicksLimit: 5,
          padding: 10,
          // Include a dollar sign in the ticks
          callback: function(value, index, values) {
            return '$' + number_format(value);
          }
        }
        
      }],
    },
  }
});



}
});



    }