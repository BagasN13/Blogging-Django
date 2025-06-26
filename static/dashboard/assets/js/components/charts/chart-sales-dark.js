//
// Charts
//

'use strict';

//
// Sales chart
//

var SalesChart = (function() {

    // Variables
    var $chart = $('#chart-sales-dark');

    // Methods
    function init($this) {
        var salesChart = new Chart($this, {
            type: 'line',
            data: {
                labels: window.userChartLabels || ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
                datasets: [{
                    label: 'Jumlah User',
                    data: window.userChartData || [],
                    borderColor: '#5e72e4',
                    backgroundColor: 'rgba(94, 114, 228, 0.1)',
                    borderWidth: 2,
                    pointBackgroundColor: '#5e72e4',
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: '#5e72e4',
                    fill: true,
                    tension: 0.4
                }]
            },
            options: {
                maintainAspectRatio: false,
                scales: {
                    yAxes: [{
                        gridLines: {
                            color: '#32325d',
                            zeroLineColor: '#32325d'
                        },
                        ticks: {
                            beginAtZero: true,
                            precision: 0
                        }
                    }],
                    xAxes: [{
                        gridLines: {
                            display: false
                        }
                    }]
                },
                legend: {
                    display: false
                },
                tooltips: {
                    callbacks: {
                        label: function(item) {
                            return 'Jumlah User: ' + item.yLabel;
                        }
                    }
                }
            }
        });

        // Save chart instance
        $this.data('chart', salesChart);
    }

    // Events
    if ($chart.length) {
        init($chart);
    }

})();
