'use strict';

(function () {
    const chartElement = document.getElementById('chart-user-growth');

    if (!chartElement) return;

    const ctx = chartElement.getContext('2d');

    const userChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: window.userChartLabels || ['Jan', 'Feb', 'Mar', 'Apr'],
            datasets: [{
                label: 'Jumlah User',
                data: window.userChartData || [0, 5, 10, 7],
                borderColor: '#5e72e4',
                backgroundColor: 'rgba(94, 114, 228, 0.1)',
                fill: true,
                tension: 0.4,
                pointBackgroundColor: '#5e72e4',
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: '#5e72e4'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        precision: 0
                    },
                    grid: {
                        color: '#32325d',
                        zeroLineColor: '#32325d'
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function (context) {
                            return 'Jumlah User: ' + context.parsed.y;
                        }
                    }
                }
            }
        }
    });
})();
