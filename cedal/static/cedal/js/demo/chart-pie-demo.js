// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = "Verdana";
Chart.defaults.global.defaultFontColor = '#858796';
Chart.defaults.global.defaultFontSize = 13;

var paramProductos = [];
var paramCantidad = [];

$.ajax({
  
  type: "get",
  dataType: 'json',
   url:  "graficoProductos",
success: function(response) {
    
    var pe = response.producto;
    
                 $.each(pe, function(i, item){
                  //const shortMonthName = moment(item.id_compra__fecha).format('MMM');
                
                 paramProductos.push(item.id_producto__nombre);
              
                 paramCantidad.push(parseFloat(item.cantidad__sum)); 
                                        
            
                
                 });


// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: paramProductos,
    datasets: [{
      data: paramCantidad,
      backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc', "#FD6973", '#5AEC06'],
      hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf', '#FC3C48', '#4DCA06'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
      borderColor: "black",
      borderWidth: 1
    }],
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    cutoutPercentage: 60,
  //   rotation: -Math.PI,
  // cutoutPercentage: 30,
  // circumference: Math.PI,
  legend: {
    position: 'bottom'
  },
  animation: {
    animateRotate: false,
    animateScale: true
  }
    // responsive: true,
    // maintainAspectRatio: false,
    // tooltips: {
    //   backgroundColor: "rgb(255,255,255)",
    //   bodyFontColor: "#858796",
    //   borderColor: '#dddfeb',
    //   borderWidth: 1,
    //   xPadding: 15,
    //   yPadding: 15,
    //   displayColors: false,
    //   caretPadding: 10,
    // },
    // legend: {
    //   display: false
    // },
    // cutoutPercentage: 80,
  },
});


}
});